
from odoo import http
from odoo.http import request

from odoo import fields, http, _
from odoo.addons.website.controllers.main import QueryURL
from odoo.http import request
from odoo.osv import expression
from odoo.tools.misc import get_lang
from odoo.tools import lazy
from odoo.exceptions import UserError


class CustomWebsiteController(http.Controller):
    
    def sitemap_event(env, rule, qs):
        if not qs or qs.lower() in '/events':
            yield {'loc': '/events'}
            
    def _get_events_search_options(self, **post):
        return {
            'displayDescription': False,
            'displayDetail': False,
            'displayExtraDetail': False,
            'displayExtraLink': False,
            'displayImage': False,
            'allowFuzzy': not post.get('noFuzzy'),
            'date': post.get('date'),
            'tags': post.get('tags'),
            'type': post.get('type'),
            'country': post.get('country'),
        }
            

    @http.route(['/event', '/event/page/<int:page>', '/events', '/events/page/<int:page>'], type='http', auth="public", website=True, sitemap=sitemap_event, readonly=True)
    def events(self, page=1, **searches):
        if searches.get('tags', '[]').count(',') > 0 and request.httprequest.method == 'GET' and not searches.get('prevent_redirect'):
            # Previously, the tags were searched using GET, which caused issues with crawlers (too many hits)
            # We replaced those with POST to avoid that, but it's not sufficient as bots "remember" crawled pages for a while
            # This permanent redirect is placed to instruct the bots that this page is no longer valid
            # Note: We allow a single tag to be GET, to keep crawlers & indexes on those pages
            # What we really want to avoid is combinatorial explosions
            # (Tags are formed as a JSON array, so we count ',' to keep it simple)
            # TODO: remove in a few stable versions (v19?), including the "prevent_redirect" param in templates
            return request.redirect('/event', code=301)

        Event = request.env['event.event']
        SudoEventType = request.env['event.type'].sudo()

        searches.setdefault('search', '')
        searches.setdefault('tags', '')
        searches.setdefault('type', 'all')
        searches.setdefault('country', 'all')
        date_all = False
        
        search = searches.get('search')
        if(search != ''):
            date_all = True
            searches.setdefault('date', 'all')
        else:
            searches.setdefault('date', 'upcoming')
        
        
        current_date = fields.Date.today()
        website = request.website
        events_per_row = 4
        max_rows = 5
        max_events = events_per_row * max_rows  # 20 eventos por página (como el step original)
        offset = (page - 1) * max_events
        
            # Dominios base
        base_domain = [
            ('website_published', '=', True),
            ('website_id', '=', website.id)
        ]
        
        search_domain = [
            '|',
            ('name', 'ilike', searches['search']),
            ('address_id.city', 'ilike', searches['search'])
        ] if searches['search'] else []

        # Obtener conteos
        incoming_domain = base_domain + [
            ('stage_id', '=', 3),  # Solo eventos confirmados
            ('date_begin', '>=', current_date)
        ] + search_domain
        
        past_domain = base_domain + [
            ('date_begin', '<', current_date)
        ] + search_domain
        
        incoming_count = Event.search_count(incoming_domain)
        past_count = Event.search_count(past_domain)
         # Manejo de eventos futuros
        incoming_offset = min(offset, incoming_count)
        incoming_limit = max(0, min(max_events, incoming_count - incoming_offset))
        
        raw_incoming_events = Event.search(
            incoming_domain,
            order='date_begin asc',
            limit=incoming_limit,
            offset=incoming_offset
        )
        
        # Calcular filas completas de eventos futuros
        incoming_len = len(raw_incoming_events)
        incoming_rows = (incoming_len + events_per_row - 1) // events_per_row
        shown_incoming_len = incoming_rows * events_per_row
        incoming_events = raw_incoming_events[:shown_incoming_len]

        # Espacio restante para eventos pasados
        remaining_rows = max(0, max_rows - incoming_rows)
        remaining_slots = remaining_rows * events_per_row

        # Manejo de eventos pasados
        previous_incoming = min(offset, incoming_count)
        previous_incoming_rows = (previous_incoming + events_per_row - 1) // events_per_row
        past_rows_displayed = max(0, max_rows * (page - 1) - previous_incoming_rows)
        past_offset = past_rows_displayed * events_per_row
        past_limit = remaining_slots
        
        past_events = []
        if remaining_slots > 0 and not date_all:
            past_events = Event.search(
                past_domain,
                order='date_begin desc',
                limit=past_limit,
                offset=past_offset
            )

        # Combinar eventos para la vista
        all_events = incoming_events + past_events
        event_count = incoming_count + past_count

        # Configuración adicional para la vista
        options = self._get_events_search_options(**searches)
        
        # Obtener detalles para filtros
        event_details = website._search_with_fuzzy("events", search, limit=1000, order='date_begin asc', options=options)[1][0]
        
        # Configuración de fechas para filtros
        no_date_domain = event_details['no_date_domain']
        dates = event_details['dates']
        for date in dates:
            if date[0] not in ['all', 'old']:
                date[3] = Event.search_count(expression.AND(no_date_domain) + search_domain + date[2])

        # Configuración de países para filtros
        no_country_domain = event_details['no_country_domain']
        countries = Event.read_group(expression.AND(no_country_domain) + search_domain, ["id", "country_id"],
            groupby="country_id", orderby="country_id")
        countries.insert(0, {
            'country_id_count': sum([int(country['country_id_count']) for country in countries]),
            'country_id': ("all", _("All Countries"))
        })

        # Configuración de tipos de evento
        search_tags = event_details['search_tags']
        current_type = None
        current_country = None

        if searches["type"] != 'all':
            current_type = SudoEventType.browse(int(searches['type']))

        if searches["country"] != 'all' and searches["country"] != 'online':
            current_country = request.env['res.country'].browse(int(searches['country']))

        # Configuración del paginador
        pager = website.pager(
            url="/event",
            url_args=searches,
            total=event_count,
            page=page,
            step=max_events,  # Usamos nuestro nuevo step basado en filas
            scope=5)

        keep = QueryURL('/event', **{
            key: value for key, value in searches.items() if (
                key == 'search' or
                (value != 'upcoming' if key == 'date' else value != 'all'))
            })

        values = {
            'current_date': current_date,
            'current_country': current_country,
            'current_type': current_type,
            'event_ids': all_events,  # Mantenemos el nombre por compatibilidad
            'upcoming_events': incoming_events,
            'past_events': past_events,
            'incoming_count': incoming_count,
            'past_count': past_count,
            'dates': dates,
            'categories': request.env['event.tag.category'].search([
                ('is_published', '=', True), '|', ('website_id', '=', website.id), ('website_id', '=', False)
            ]),
            'countries': countries,
            'pager': pager,
            'searches': searches,
            'search_tags': search_tags,
            'keep': keep,
            'search_count': event_count,
            'original_search': searches['search'],
            'website': website,
            'events_per_row': events_per_row,
        }

        return request.render("website_event.index", values)
    
# Event card

    
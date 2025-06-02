# -*- coding: utf-8 -*-

from odoo import _, models, fields, api
from odoo.exceptions import MissingError


class EventSchedule(models.Model):
    _name = 'event.schedule'
    _description = 'Event Schedule'

    name = fields.Char(string="Title", required=True)
    start = fields.Datetime(string="Begin", required=True)
    stop = fields.Datetime(string="End", required=True)
    locations = fields.Many2many(
        'res.partner',
        'event_schedule_res_partner_locations_rel',  # nombre de la tabla de relación (¡debe ser única!)
        'schedule_id',  # columna que apunta a event.schedule
        'partner_id',   # columna que apunta a res.partner
        string="Locations"
    )
    description = fields.Text(string="Description")
    partner_ids = fields.Many2many('res.partner', string="Participants")
    event_id = fields.Many2one('event.event', string="Evento", ondelete='cascade')
    user_id = fields.Many2one('res.users', string='Responsable', default=lambda self: self._get_default_user())

    
    @api.model
    def _get_default_user(self):
        # Si hay un contexto con 'default_event_id', lo usamos para heredar el user_id del evento
        event = self.env.context.get('default_event_id') and self.env['event.event'].browse(self.env.context['default_event_id'])
        return event.user_id.id if event and event.user_id else self.env.user.id
    
    @api.model_create_multi
    def create(self, vals_list):
        record = super().create(vals_list)
        if record.event_id:
            record.event_id.message_post(
                body=_("Se ha añadido un nuevo horario: %s, 🕒 %s - %s") % (
                    record.name,
                    record.start.strftime('%Y-%m-%d %H:%M'),
                    record.stop.strftime('%Y-%m-%d %H:%M')
                )
            )
        return record
    
    @api.model_create_multi
    def write(self, vals_list):
        for rec in self:
            old_values = rec.read()[0]  # guardar valores antes del cambio
            result = super(EventSchedule, rec).write(vals_list)
            if rec.event_id:
                changes = []
                for field in ['name', 'start', 'stop', 'description']:
                    if field in vals_list:
                        changes.append(f"{field}: {old_values[field]} → {rec[field]}")
                if changes:
                    rec.event_id.message_post(
                        body=_("Horario actualizado: %s %s") % (
                            rec.name,
                            "".join(changes)
                        )
                    )
        return result

    @api.model_create_multi
    def unlink(self):
        for rec in self:
            if rec.event_id:
                rec.event_id.message_post(
                    body=_(" Se ha eliminado el horario: %s (%s - %s)") % (
                        rec.name,
                        rec.start.strftime('%Y-%m-%d %H:%M'),
                        rec.stop.strftime('%Y-%m-%d %H:%M')
                    )
                )
        return super().unlink()

    
    
class EventHotelExtension(models.Model):
    _inherit = 'event.event'
    
    horarios = fields.One2many(
    'event.schedule',
    'event_id',
    string="Horarios del evento",
    )
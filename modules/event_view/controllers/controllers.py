# -*- coding: utf-8 -*-
# from odoo import http


# class EventView(http.Controller):
#     @http.route('/event_view/event_view', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/event_view/event_view/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('event_view.listing', {
#             'root': '/event_view/event_view',
#             'objects': http.request.env['event_view.event_view'].search([]),
#         })

#     @http.route('/event_view/event_view/objects/<model("event_view.event_view"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('event_view.object', {
#             'object': obj
#         })


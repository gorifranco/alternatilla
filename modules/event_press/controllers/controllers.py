# -*- coding: utf-8 -*-
# from odoo import http


# class EventPress(http.Controller):
#     @http.route('/event_press/event_press', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/event_press/event_press/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('event_press.listing', {
#             'root': '/event_press/event_press',
#             'objects': http.request.env['event_press.event_press'].search([]),
#         })

#     @http.route('/event_press/event_press/objects/<model("event_press.event_press"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('event_press.object', {
#             'object': obj
#         })


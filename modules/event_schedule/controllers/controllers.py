# -*- coding: utf-8 -*-
# from odoo import http


# class EventSchedule(http.Controller):
#     @http.route('/event_schedule/event_schedule', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/event_schedule/event_schedule/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('event_schedule.listing', {
#             'root': '/event_schedule/event_schedule',
#             'objects': http.request.env['event_schedule.event_schedule'].search([]),
#         })

#     @http.route('/event_schedule/event_schedule/objects/<model("event_schedule.event_schedule"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('event_schedule.object', {
#             'object': obj
#         })


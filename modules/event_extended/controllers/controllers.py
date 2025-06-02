# -*- coding: utf-8 -*-
# from odoo import http


# class EventHotel(http.Controller):
#     @http.route('/event_hotel/event_hotel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/event_hotel/event_hotel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('event_hotel.listing', {
#             'root': '/event_hotel/event_hotel',
#             'objects': http.request.env['event_hotel.event_hotel'].search([]),
#         })

#     @http.route('/event_hotel/event_hotel/objects/<model("event_hotel.event_hotel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('event_hotel.object', {
#             'object': obj
#         })


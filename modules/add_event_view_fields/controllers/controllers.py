# -*- coding: utf-8 -*-
# from odoo import http


# class AddEventViewFields(http.Controller):
#     @http.route('/add_event_view_fields/add_event_view_fields', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/add_event_view_fields/add_event_view_fields/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('add_event_view_fields.listing', {
#             'root': '/add_event_view_fields/add_event_view_fields',
#             'objects': http.request.env['add_event_view_fields.add_event_view_fields'].search([]),
#         })

#     @http.route('/add_event_view_fields/add_event_view_fields/objects/<model("add_event_view_fields.add_event_view_fields"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('add_event_view_fields.object', {
#             'object': obj
#         })


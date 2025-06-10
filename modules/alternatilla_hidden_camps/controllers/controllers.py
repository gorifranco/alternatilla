# -*- coding: utf-8 -*-
# from odoo import http


# class AlternatillaHiddenCamps(http.Controller):
#     @http.route('/alternatilla_hidden_camps/alternatilla_hidden_camps', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alternatilla_hidden_camps/alternatilla_hidden_camps/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('alternatilla_hidden_camps.listing', {
#             'root': '/alternatilla_hidden_camps/alternatilla_hidden_camps',
#             'objects': http.request.env['alternatilla_hidden_camps.alternatilla_hidden_camps'].search([]),
#         })

#     @http.route('/alternatilla_hidden_camps/alternatilla_hidden_camps/objects/<model("alternatilla_hidden_camps.alternatilla_hidden_camps"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alternatilla_hidden_camps.object', {
#             'object': obj
#         })


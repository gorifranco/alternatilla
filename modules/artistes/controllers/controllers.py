# -*- coding: utf-8 -*-
# from odoo import http


# class Artistes(http.Controller):
#     @http.route('/artistes/artistes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/artistes/artistes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('artistes.listing', {
#             'root': '/artistes/artistes',
#             'objects': http.request.env['artistes.artistes'].search([]),
#         })

#     @http.route('/artistes/artistes/objects/<model("artistes.artistes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('artistes.object', {
#             'object': obj
#         })


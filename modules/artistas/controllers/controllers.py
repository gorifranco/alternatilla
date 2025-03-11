# -*- coding: utf-8 -*-
# from odoo import http


# class Artistas(http.Controller):
#     @http.route('/artistas/artistas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/artistas/artistas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('artistas.listing', {
#             'root': '/artistas/artistas',
#             'objects': http.request.env['artistas.artistas'].search([]),
#         })

#     @http.route('/artistas/artistas/objects/<model("artistas.artistas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('artistas.object', {
#             'object': obj
#         })


# -*- coding: utf-8 -*-
# from odoo import http


# class Roadmap(http.Controller):
#     @http.route('/roadmap/roadmap', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/roadmap/roadmap/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('roadmap.listing', {
#             'root': '/roadmap/roadmap',
#             'objects': http.request.env['roadmap.roadmap'].search([]),
#         })

#     @http.route('/roadmap/roadmap/objects/<model("roadmap.roadmap"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('roadmap.object', {
#             'object': obj
#         })


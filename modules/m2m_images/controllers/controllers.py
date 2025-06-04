# -*- coding: utf-8 -*-
# from odoo import http


# class M2mImages(http.Controller):
#     @http.route('/m2m_images/m2m_images', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/m2m_images/m2m_images/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('m2m_images.listing', {
#             'root': '/m2m_images/m2m_images',
#             'objects': http.request.env['m2m_images.m2m_images'].search([]),
#         })

#     @http.route('/m2m_images/m2m_images/objects/<model("m2m_images.m2m_images"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('m2m_images.object', {
#             'object': obj
#         })


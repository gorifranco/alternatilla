# -*- coding: utf-8 -*-
# from odoo import http


# class ContactPublic(http.Controller):
#     @http.route('/contact_public/contact_public', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contact_public/contact_public/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('contact_public.listing', {
#             'root': '/contact_public/contact_public',
#             'objects': http.request.env['contact_public.contact_public'].search([]),
#         })

#     @http.route('/contact_public/contact_public/objects/<model("contact_public.contact_public"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contact_public.object', {
#             'object': obj
#         })


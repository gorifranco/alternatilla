# -*- coding: utf-8 -*-
# from odoo import http


# class AddAvatarImageEvent(http.Controller):
#     @http.route('/add_avatar_image_event/add_avatar_image_event', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/add_avatar_image_event/add_avatar_image_event/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('add_avatar_image_event.listing', {
#             'root': '/add_avatar_image_event/add_avatar_image_event',
#             'objects': http.request.env['add_avatar_image_event.add_avatar_image_event'].search([]),
#         })

#     @http.route('/add_avatar_image_event/add_avatar_image_event/objects/<model("add_avatar_image_event.add_avatar_image_event"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('add_avatar_image_event.object', {
#             'object': obj
#         })


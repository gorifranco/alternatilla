# -*- coding: utf-8 -*-
# from odoo import http


# class WebFonart(http.Controller):
#     @http.route('/web_fonart/web_fonart', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/web_fonart/web_fonart/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('web_fonart.listing', {
#             'root': '/web_fonart/web_fonart',
#             'objects': http.request.env['web_fonart.web_fonart'].search([]),
#         })

#     @http.route('/web_fonart/web_fonart/objects/<model("web_fonart.web_fonart"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('web_fonart.object', {
#             'object': obj
#         })

from odoo import http
from odoo.http import request


class CustomWebsiteController(http.Controller):
    
    @http.route('/', type='http', auth="public")
    def index(self, **kwargs):
        
        print(">>> Se ha ejecutado el controlador personalizado de Fonart")
        return "Hola mundo"

    @http.route('/tomeu', type='http', auth="public")
    def tomeu(self, **kwargs):
        
        print(">>> Se ha ejecutado el controlador personalizado de Fonart")
        return "Hola mundo"


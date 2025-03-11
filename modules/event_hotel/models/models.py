# -*- coding: utf-8 -*-

from odoo import models, fields

class EventHotelExtension(models.Model):
    _inherit = 'event.event'

    hotel_id = fields.Many2one('res.partner', string="Hotel", domain=[('is_company', '=', True)])
    comentario_hotel = fields.Text(string="Comentario")
    promotor_id = fields.Many2one('res.partner', string="Promotor")
    link_entradas = fields.Char(string="Link Entradas")
    apertura_de_puertas = fields.Date(string="Apertura de Puertas")

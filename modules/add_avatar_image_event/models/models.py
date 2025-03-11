# -*- coding: utf-8 -*-

from odoo import models, fields

class EventHotelExtension(models.Model):
    _inherit = 'event.event'

    avatar_image = fields.Image(string="Avatar", max_width=1024, max_height=1024)
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Image(models.Model):
    _name = "m2m_images"
    _order = "id desc"

    name = fields.Char(string="Name")
    
    image = fields.Image(string="Image", max_width=1920, max_height=1920)
    image_1024 = fields.Image("Image 1024px", related="image", max_width=1024, max_height=1024, store=True)
    image_256 = fields.Image("Image 256px", related="image", max_width=256, max_height=256, store=True)
    image_64 = fields.Image("Image 64px", related="image", max_width=64, max_height=64, store=True)

    uri = fields.Char(compute="_compute_uri", store=True)

    @api.depends('image')
    def _compute_uri(self):
        for rec in self:
            rec.uri = rec.image and f"/web/image/{rec._name}/{rec.id}/image" or False
            



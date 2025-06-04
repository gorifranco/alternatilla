# -*- coding: utf-8 -*-

from odoo import models, fields


class EventViewExtension(models.Model):
    _inherit = 'event.event'
    
    cover_image = fields.Image(string="Image", max_width=1920, max_height=1920)
    cover_image_1024 = fields.Image("Image 1024px", related="image", max_width=1024, max_height=1024, store=True)
    cover_image_256 = fields.Image("Image 256px", related="image", max_width=256, max_height=256, store=True)
    
    imatges_web = fields.Many2many('m2m_images', string="Imatges web")
    videos = fields.Many2many('website.video', string="Videos")
    text_principal = fields.Html(string="Text Principal")
    imatges_laterals = fields.Many2many('image', string="Imatges laterals")
    cartells = fields.Many2many('image', string="Cartells")
    compromesos = fields.Many2many('res.partner', string="Compromesos")
    patrocinadors = fields.Many2many('res.partner', string="Patrocinadors")
    colaboradors = fields.Many2many('res.partner', string="Colaboradors")
    
    
class EventVideos(models.Model):
    _name = "website.video"
    _description = "Videos"
    
    url = fields.Char(string="Video", required=True)
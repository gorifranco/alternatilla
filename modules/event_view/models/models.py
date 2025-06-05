# -*- coding: utf-8 -*-

from odoo import models, fields


class EventViewExtension(models.Model):
    _inherit = 'event.event'
    
    cover_image = fields.Image(string="Image", max_width=1920, max_height=1920)
    cover_image_1024 = fields.Image("Image 1024px", related="cover_image", max_width=1024, max_height=1024, store=True)
    cover_image_256 = fields.Image("Image 256px", related="cover_image", max_width=256, max_height=256, store=True)
    
    imatges_web = fields.Many2many('m2m_images', string="Imatges web")
    videos = fields.One2many('website.video', 'event_id', string="Videos")
    text_principal = fields.Html(string="Text Principal")
    imatges_laterals = fields.Many2many(
        'm2m_images', 
        'event_image_laterals_rel',
        'event_id', 'image_id', 
        string="Imatges laterals"
    )
    cartells = fields.Many2many(
        'm2m_images', 
        'event_image_cartells_rel',
        'event_id', 'image_id', 
        string="Cartells"
    )

    compromesos = fields.Many2many(
    'res.partner',
    'event_event_res_partner_compromesos_rel',
    'event_id',
    'partner_id',
    string="Compromesos"
    )

    patrocinadors = fields.Many2many(
        'res.partner',
        'event_event_res_partner_patrocinadors_rel',
        'event_id',
        'partner_id',
        string="Patrocinadors"
    )

    colaboradors = fields.Many2many(
        'res.partner',
        'event_event_res_partner_colaboradors_rel',
        'event_id',
        'partner_id',
        string="Colaboradors"
    )
    
    
class EventVideos(models.Model):
    _name = "website.video"
    _description = "Videos"
    
    url = fields.Char(string="Video", required=True)
    event_id = fields.Many2one('event.event', string="Event")
    
# -*- coding: utf-8 -*-

from odoo import models, fields


class EventViewExtension(models.Model):
    _inherit = 'event.event'
    
    cover_image = fields.Image(string="Cover Image", max_width=1920, max_height=1920)
    cover_image_1024 = fields.Image("Image 1024px", related="cover_image", max_width=1024, max_height=1024, store=True)
    cover_image_256 = fields.Image("Image 256px", related="cover_image", max_width=256, max_height=256, store=True)
    
    web_images = fields.Many2many('m2m_images', string="Web Images")
    videos = fields.One2many('website.video', 'event_id', string="Videos")
    main_text = fields.Html(string="Main Text", translate=True)
    side_images = fields.Many2many(
        'm2m_images', 
        'event_image_laterals_rel',
        'event_id', 'image_id', 
        string="Side Images"
    )
    posters = fields.Many2many(
        'm2m_images', 
        'event_image_posters_rel',
        'event_id', 'image_id', 
        string="Posters"
    )

    commitments = fields.Many2many(
        'res.partner',
        'event_event_res_partner_commitments_rel',
        'event_id',
        'partner_id',
        string="Commitments"
    )

    sponsors = fields.Many2many(
        'res.partner',
        'event_event_res_partner_sponsors_rel',
        'event_id',
        'partner_id',
        string="Sponsors"
    )

    collaborators = fields.Many2many(
        'res.partner',
        'event_event_res_partner_collaborators_rel',
        'event_id',
        'partner_id',
        string="Collaborators"
    )
    
    
class EventVideos(models.Model):
    _name = "website.video"
    _description = "Videos"
    
    url = fields.Char(string="Video URL", required=True)
    event_id = fields.Many2one('event.event', string="Related Event")
    
    
class EventVideos(models.Model):
    _name = "website.video"
    _description = "Videos"
    
    url = fields.Char(string="Video", required=True)
    event_id = fields.Many2one('event.event', string="Event")
    
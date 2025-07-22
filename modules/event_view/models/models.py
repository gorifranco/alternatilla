# -*- coding: utf-8 -*-

from odoo import models, fields


class EventViewExtension(models.Model):
    _inherit = 'event.event'
    
    cover_image = fields.Image(string="Cover Image", max_width=1920, max_height=1920)
    cover_image_1024 = fields.Image("Image 1024px", related="cover_image", max_width=1024, max_height=1024, store=True)
    cover_image_512 = fields.Image("Image 512px", related="cover_image", max_width=512, max_height=512, store=True)
    
    web_images = fields.Many2many('ir.attachment', 'web_image_event_rel', 'event_id', 'attachment_id', string="Web Images")
    videos = fields.One2many('event.video', 'event_id', string="Videos")
    main_text = fields.Html(string="Main Text", translate=True)
    side_images = fields.Many2many(
        'ir.attachment',
        'event_side_images_rel',
        'event_id', 'attachment_id',
        string="Side Images"
    )
    posters = fields.Many2many(
        'ir.attachment',
        'event_posters_rel',
        'event_id', 'attachment_id', 
        string="Posters"
    )

    commitment_ids = fields.One2many('event.commitment', 'event_id', string="Commitments")
    sponsors_ids = fields.One2many('event.sponsor', 'event_id', string="Sponsors")
    collaborators_ids = fields.One2many('event.collaborator', 'event_id', string="Collaborators")

    
    
class EventVideos(models.Model):
    _name = "event.video"
    _description = "Videos"
    
    url = fields.Char(string="Video", required=True)
    event_id = fields.Many2one('event.event', string="Event")
    
class EventCommitment(models.Model):
    _name = 'event.commitment'
    _order = 'sequence'

    event_id = fields.Many2one('event.event', ondelete='cascade', required=True)
    partner_id = fields.Many2one('res.partner', required=True)
    sequence = fields.Integer(default=0)
    
class EventSponsor(models.Model):
    _name = 'event.sponsor'
    _order = 'sequence'

    event_id = fields.Many2one('event.event', ondelete='cascade', required=True)
    partner_id = fields.Many2one('res.partner', required=True)
    sequence = fields.Integer(default=0)
    
class EventCollaborator(models.Model):
    _name = 'event.collaborator'
    _order = 'sequence'

    event_id = fields.Many2one('event.event', ondelete='cascade', required=True)
    partner_id = fields.Many2one('res.partner', required=True)
    sequence = fields.Integer(default=0)
    
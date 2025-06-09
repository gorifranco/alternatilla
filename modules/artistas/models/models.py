# -*- coding: utf-8 -*-


from odoo import models, fields


class ArtistTag(models.Model):
    _name = 'artist.tags'
    _description = 'Artist Tag'

    name = fields.Char(required=True)

class Artist(models.Model):
    _name = 'artist.artist'
    _description = 'Artist'

    partner_id = fields.Many2one('res.partner', string="Contact")
    description = fields.Text(string="Description")
    tag_ids = fields.Many2many('artist.tags', string="Tags")
    

class Band(models.Model):
    _name = 'artist.band'
    _description = 'Music Band'
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner', string="Contact", required=True)
    description = fields.Text(string="Description")
    tag_ids = fields.Many2many('artist.tags', string="Tags")
    company_id = fields.Many2one('res.company', string="Company")
    manager_id = fields.Many2one('res.partner', string="Manager")
    artist_ids = fields.Many2many('artist.artist', string="Artists")
    members = fields.Html(string="Members")
    image = fields.Image(string="Image", max_width=1920, max_height=1920)
    image_256 = fields.Image("Image 256px", related="image", max_width=256, max_height=256, store=True)
    image_64 = fields.Image("Image 64px", related="image", max_width=64, max_height=64, store=True)
    

class EventBandExtension(models.Model):
    _inherit = 'event.event'

    bands = fields.Many2many('artist.band', string="Bands")
    


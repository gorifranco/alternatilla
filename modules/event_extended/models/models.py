# -*- coding: utf-8 -*-

from odoo import models, fields

class EventHotelExtension(models.Model):
    _inherit = 'event.event'

    hotel_id = fields.Many2one('res.partner', string="Hotel", domain=[('is_company', '=', True)], tracking=True)
    route_sheet_comment = fields.Html(string="Route Sheet Comment", tracking=True)
    hotel_comment = fields.Html(string="Hotel Comment", tracking=True)
    room_distribution = fields.One2many('event.room', 'event_id', string="Room Distribution", tracking=True)

    promoter_id = fields.Many2one('res.partner', string="Promoter", tracking=True)
    ticket_link = fields.Char(string="Ticket Link", tracking=True)
    free_entry = fields.Boolean(string="Free Entry", tracking=True)
    sold_out = fields.Boolean(string="Sold Out", tracking=True)
    doors_open = fields.Date(string="Doors Open", tracking=True)
    technicians = fields.One2many('event.technician', 'event_id', string="Technicians", tracking=True)
    festival_id = fields.Many2one('event.festival', string="Festival", tracking=True)
    

class Technician(models.Model):
    _name = 'event.technician'
    _description = 'Technician'
    
    name = fields.Char(string="Name", required=True)
    contact = fields.Many2one("res.partner", string="Contact")
    type = fields.Char(string="Type")
    event_id = fields.Many2one('event.event', string="Event")
    

class Room(models.Model):
    _name = 'event.room'
    _description = 'Room'
    
    description = fields.Text(string="Description")
    room_type = fields.Char(string="Room Type")
    people = fields.Many2many('res.partner', string="People")
    event_id = fields.Many2one('event.event', string="Event")
    

class Festival(models.Model):
    _name = 'event.festival'
    _description = 'Festival'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string="Name", required=True, tracking=True)
    date_begin = fields.Date(string="Date Begin", tracking=True)
    date_end = fields.Date(string="Date End", tracking=True)
    presentation = fields.Html(string="Presentation", tracking=True)
    is_active = fields.Boolean(string="Is Active", tracking=True)
    Url_magazine = fields.Char(string="Url Magazine", tracking=True)
    company_id = fields.Many2one('res.company', string="Company", tracking=True)
    image = fields.Image(string="Image", tracking=True)
    image_256 = fields.Image(string="Image 256", max_height="256", max_width="256", related='image', store=True)
    cover_magazine = fields.Image(string="Cover Magazine", related='image', store=True, tracking=True)
    cover_magazine_640 = fields.Image(string="Cover Magazine 640", max_height="640", max_width="640", related='image', store=True)
    

    

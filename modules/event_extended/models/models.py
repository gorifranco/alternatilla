# -*- coding: utf-8 -*-

from odoo import models, fields

class EventHotelExtension(models.Model):
    _inherit = 'event.event'

    hotel_id = fields.Many2one('res.partner', string="Hotel", domain=[('is_company', '=', True)], Track=True)
    route_sheet_comment = fields.Html(string="Route Sheet Comment", Track=True)
    hotel_comment = fields.Html(string="Hotel Comment", Track=True)
    room_distribution = fields.One2many('event.room', 'event_id', string="Room Distribution", Track=True)

    promoter_id = fields.Many2one('res.partner', string="Promoter", Track=True)
    ticket_link = fields.Char(string="Ticket Link", Track=True)
    free_entry = fields.Boolean(string="Free Entry", Track=True)
    sold_out = fields.Boolean(string="Sold Out", Track=True)
    doors_open = fields.Date(string="Doors Open", Track=True)
    technicians = fields.One2many('event.technician', 'event_id', string="Technicians", Track=True)
    

class Technician(models.Model):
    _name = 'event.technician'
    _description = 'Technician'
    
    name = fields.Char(string="Name")
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
    

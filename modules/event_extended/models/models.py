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
    

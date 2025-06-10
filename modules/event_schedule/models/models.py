# -*- coding: utf-8 -*-

from odoo import _, models, fields
    
    
class EventHotelExtension(models.Model):
    _inherit = 'event.event'
    
    schedule = fields.One2many('calendar.event', 'event_id', string="Schedule", tracking=True)
    

class CalendarEvent(models.Model):
    _inherit = 'calendar.event'
    
    event_id = fields.Many2one('event.event', string="Event", ondelete='cascade')
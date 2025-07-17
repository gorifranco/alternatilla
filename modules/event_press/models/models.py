# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class event_press(models.Model):
    _name = 'event.event_press'
    _description = 'Press for events'
    _sql_constraints = [
        ('unique_event_press', 'UNIQUE(event)', 'Each event can only have one press release.'),
    ]

    # name = fields.Char()
    event = fields.Many2one('event.event')
    images = fields.Many2many('ir.attachment', string='Images')
    press_note = fields.Html(string='Press note')
    call = fields.Html(string='Call') #convocatòria
    
    @api.constrains('event')
    def _check_unique_event(self):
        for record in self:
            existing = self.search([
                ('event', '=', record.event.id),
                ('id', '!=', record.id)
            ])
            if existing:
                raise ValidationError('This event already has a press release.')
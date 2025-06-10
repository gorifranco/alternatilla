# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class alternatilla_hidden_camps(models.Model):
#     _name = 'alternatilla_hidden_camps.alternatilla_hidden_camps'
#     _description = 'alternatilla_hidden_camps.alternatilla_hidden_camps'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


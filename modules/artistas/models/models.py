# -*- coding: utf-8 -*-


from odoo import models, fields


class ArtistaTag(models.Model):
    _name = 'artistas.tags'
    _description = 'Etiqueta de Artista'

    name = fields.Char(required=True)

class artistes(models.Model):
    _name = 'artistas.artistas'
    _description = 'artistas.artistas'

    partner_id = fields.Many2one('res.partner', string="Contacto")
    descripcion = fields.Text(string="Descripción")
    tags_ids = fields.Many2many('artistas.tags', string="Tags")
    


class grupos(models.Model):
    _name = 'artistas.grupos'
    _description = 'Grupos de música'

    partner_id = fields.Many2one('res.partner', string="Contacto")
    descripcion = fields.Text(string="Descripción")
    tags_ids = fields.Many2many('artistas.tags', string="Tags")
    website_id = fields.Many2one('website', string="Website")
    manager_id = fields.Many2one('res.partner', string="Manager")
    artistas_ids = fields.Many2many('artistas.artistas', string="Artistas")
    componentes = fields.Html(string="Componentes")
    
    
    #Adds the group to the events
class EventGroupExtension(models.Model):
    _inherit = 'event.event'

    grupo = fields.Many2one('artistas.grupos', string="Grupo")
    


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
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner', string="Contacto")
    descripcion = fields.Text(string="Descripción")
    tags_ids = fields.Many2many('artistas.tags', string="Tags")
    company_id = fields.Many2one('res.company', string="Compañía")
    manager_id = fields.Many2one('res.partner', string="Manager")
    artistas_ids = fields.Many2many('artistas.artistas', string="Artistas")
    componentes = fields.Html(string="Componentes")
    image = fields.Image(string="Imagen", max_width=1920, max_height=1920)
    image_256 = fields.Image("Imagen 256px", related="image", max_width=256, max_height=256, store=True)
    image_64 = fields.Image("Imagen 64px", related="image", max_width=64, max_height=64, store=True)
    
    
    #Adds the group to the events
class EventGroupExtension(models.Model):
    _inherit = 'event.event'

    grupos = fields.Many2many('artistas.grupos', string="Grupos")
    


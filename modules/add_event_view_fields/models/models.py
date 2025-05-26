# -*- coding: utf-8 -*-

from odoo import models, fields
 
class EventViewExtension(models.Model):
    _inherit = 'event.event'
    
    imagenes_laterales = fields.Many2many(
        'ir.attachment', 
        string="Imágenes laterales", 
        domain=[('mimetype', 'ilike', 'image')]
    )
    
    videos = fields.Char(string="Videos")
    imagen_superior = fields.Image(string="Imagen superior")
    comprometidos = fields.Many2many(
        'res.partner', 
        'event_comprometidos_rel',  # Nombre de la tabla intermedia
        'event_id',  # Columna que referencia event.event
        'partner_id',  # Columna que referencia res.partner
        string="Comprometidos"
    )

    patrocinadores = fields.Many2many(
        'res.partner', 
        'event_patrocinadores_rel',  # Nombre de la tabla intermedia
        'event_id',  
        'partner_id',  
        string="Patrocinadores"
    )

    colaboradores = fields.Many2many(
        'res.partner', 
        'event_colaboradores_rel',  # Nombre de la tabla intermedia
        'event_id',  
        'partner_id',  
        string="Colaboradores"
    )


    def write(self, vals):
        res = super().write(vals)
        if 'imagenes_laterales' in vals:
            self._set_attachments_public()
        return res

    def _set_attachments_public(self):
        """Fuerza a que los archivos adjuntos sean públicos"""
        for attachment in self.imagenes_laterales:
            attachment.public = True
            
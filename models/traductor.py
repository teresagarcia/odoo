# -*- coding: utf-8 -*-

from odoo import models,fields
    
class traductor(models.Model):
    _name = 'tradus.traductor'
    _inherit = 'tradus.persona'
    fecha_incorporacion = fields.Date()
    id_idiomas = fields.Many2many(string= "idiomas",comodel_name='tradus.idioma',relation = 'rel_traductor_idiomas',column1='traductor', column2='idioma')

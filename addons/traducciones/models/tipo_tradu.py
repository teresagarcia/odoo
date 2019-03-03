# -*- coding: utf-8 -*-

from odoo import models,fields
    
class tipo_tradu(models.Model):
    _name = 'tradus.tipo_tradu'
    nombre = fields.Char()
    ids_encargos = fields.One2many(
        'tradus.encargo', 'id_tipo', String="encargo")
# -*- coding: utf-8 -*-

from odoo import models,fields
    
class idioma(models.Model):
    _name = 'tradus.idioma'
    nombre = fields.Char()

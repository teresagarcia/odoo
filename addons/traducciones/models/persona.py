# -*- coding: utf-8 -*-

from odoo import models,fields
    
class persona(models.Model):
    _name = 'tradus.persona'
    dni =  fields.Char()
    nombre = fields.Char()
    apellidos = fields.Char()

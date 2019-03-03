# -*- coding: utf-8 -*-

from odoo import models,fields
    
class cliente(models.Model):
    _name = 'tradus.cliente'
    _inherit = 'base.empresa'
    direccion = fields.Char()
    persona_contacto = fields.Char()
    telefono = fields.Char()
    ids_encargos = fields.One2many(
        'tradus.encargo', 'id_cliente', String="encargo")


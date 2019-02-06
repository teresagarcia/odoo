# -*- coding: utf-8 -*-

from odoo import models,fields
    
class cliente(models.Model):
    _name = 'tradus.cliente'
    _inherit = 'tradus.persona'
    direccion = fields.Char()
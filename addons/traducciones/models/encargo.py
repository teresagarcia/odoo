# -*- coding: utf-8 -*-

from odoo import models, fields


class encargo(models.Model):
   _name = 'tradus.encargo'
   fecha_entrega = fields.Date()
   precio = fields.Integer()
   id_cliente = fields.Many2one('tradus.cliente', string="cliente")
   id_idioma = fields.Many2one('tradus.idioma', string="idioma")
   id_tipo = fields.Many2one('tradus.tipo_tradu', string="tipo")
   id_traductores = fields.Many2many(string="traductores", comodel_name='tradus.traductor',
                                     relation='rel_encargo_traductor', column1='encargo', column2='traductor')



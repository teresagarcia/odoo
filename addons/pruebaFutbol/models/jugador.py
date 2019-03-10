# -*- coding: utf-8 -*-

from odoo import models, fields


class jugador(models.Model):
    _name = 'fut.jugador'
    nombre = fields.Char()
    numero = fields.Integer()
    id_equipo = fields.Many2one('fut.equipo', string="equipo")
    fecha_incorporacion = fields.date()
    # años: calculado
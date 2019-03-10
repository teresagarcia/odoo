# -*- coding: utf-8 -*-

from odoo import models, fields


class torneo(models.Model):
    _name = 'fut.torneo'
    nombre = fields.Char()
    fecha_inicio = fields.date()
    fecha_final = fields.date()
    # ids_equipos = N:N
    # ids_partidos = 1:N
    # años: calculado

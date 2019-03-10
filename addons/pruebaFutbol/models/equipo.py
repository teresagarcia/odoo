# -*- coding: utf-8 -*-

from odoo import models, fields


class equipo(models.Model):
    _name = 'fut.equipo'
    _inherit = 'base.empresa'
    presupuesto = fields.Integer()
    categoria = fields.Char()
    ids_jugadores = fields.One2many(
        'fut.jugador', 'id_equipo', String="jugador")
    ids_local = fields.One2many(
        'fut.partido', 'id_local', String="local")
    ids_visitante = fields.One2many(
        'fut.partido', 'id_visitante', String="visitante")
    europa = fields.Boolean()
    observaciones = fields.Text()

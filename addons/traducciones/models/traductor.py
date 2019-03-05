# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta, date, datetime
from dateutil.relativedelta import relativedelta


class traductor(models.Model):
    _name = 'tradus.traductor'
    dni = fields.Char()
    nombre = fields.Char()
    apellidos = fields.Char()
    fecha_incorporacion = fields.Date()
    id_idiomas = fields.Many2many(string="idiomas", comodel_name='tradus.idioma',
                                  relation='rel_traductor_idiomas', column1='traductor', column2='idioma')
    tiempo = fields.Integer(compute="_value_pc", store=True)

    @api.onchange('fecha_incorporacion')
    def _value_pc(self):
        for r in self:
            if r.fecha_incorporacion:
                dt = r.fecha_incorporacion
                d1 = datetime.strptime(dt, "%Y-%m-%d").date()
                self.tiempo = relativedelta(date.today(), d1).years
                return {
                    'warning': {
                    'title': "Tiempo",
                    'message': "Tiempo en la empresa actualizado",
                    },
                }
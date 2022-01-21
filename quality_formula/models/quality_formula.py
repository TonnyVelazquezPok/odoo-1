# -*- coding: utf-8 -*-

from odoo import models, fields, api


class QualityFormula(models.Model):
    _name = 'quality.formula'
    _description = 'Quality Formula'

    name = fields.Char(
        'Formula Abbreviation',
        required=True
    )
    description = fields.Char('Description')
    formula = fields.Char(
        'Formula',
        required=True
    )
    notes = fields.Text('Notes')

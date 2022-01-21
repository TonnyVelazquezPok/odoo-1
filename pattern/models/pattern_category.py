# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PatternFiles(models.Model):
    _name = 'pattern.category'
    _description = 'Material category'

    name = fields.Char(
        string='Category',
        size=64,
        required=False,
        readonly=False
    )
    revision_time = fields.Integer(
        string='Review period (Days)',
        required=True, default=30
    )
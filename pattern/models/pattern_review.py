# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PatternReview(models.Model):
    _name = 'pattern.review'
    _description = 'Models Review'
    _order = 'date desc'

    user_id = fields.Many2one(
        comodel_name='res.partner',
        string='User'
    )
    date = fields.Date(string='Date')
    pattern_id = fields.Many2one(
        comodel_name='pattern',
        string='Model'
    )
    result = fields.Selection(
        [
            ('optimum', 'Optimum'),
            ('acceptable', 'Acceptable'),
            ('deteriorated', 'Deteriorated'),
            ('repair', 'Repair'),
        ],
        string='Result',
        required=True)
    notes = fields.Char(string='Notes')

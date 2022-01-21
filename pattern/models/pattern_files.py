# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PatternFiles(models.Model):
    _name = 'pattern.files'
    _description = 'Pattern files'

    user_id = fields.Many2one(
        comodel_name='res.partner',
        string='User'
    )
    pattern_id = fields.Many2one(
        comodel_name='pattern',
        string='Pattern'
    )
    file_type = fields.Selection(
        string='Type',
        selection=[
        ('video', 'Video'),
        ('picture', 'Picture'),
        ('document', 'Document')
        ]
    )
    file = fields.Many2many(
        'ir.attachment',
        string='Documents'
    )
    component = fields.Char(
        string='Component',
        help='Name component part'
    )
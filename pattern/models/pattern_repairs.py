# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PatternRepairs(models.Model):
    _name = 'pattern.repairs'

    _description = 'Model reappearance record'
    _order = 'date_send desc'

    user_id = fields.Many2one(
        comodel_name='res.partner',
        string='User'
    )
    date_send = fields.Date(
        string='Reparation date',
        default=fields.Date.today(),
        required=True
    )
    date_return = fields.Date(string='Return date')
    pattern_id = fields.Many2one(
        comodel_name='pattern',
        string='Model'
    )
    notes = fields.Char(
        string='Notes',
        required=True
    )

    @api.model
    def create(self, vals):
        repair = super().create(vals)
        pattern = self.env['pattern'].search(
            [('id', '=', repair.pattern_id.id)]) 
        pattern.location = 'provider'
        pattern.state = 'repair'
        pattern.release = False
        return repair

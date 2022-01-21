# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

class Pattern(models.Model):
    _name = 'pattern'
    _description = 'Control de Modelos'
    _inherit = ['mail.thread']

    name = fields.Char(
        string='Model',
        compute='_compute_patter_name'
    )
    product_id = fields.Many2one(
        comodel_name='product.product',
        string='UID POK'
    )
    product_tag_ids = fields.Many2many(
        'pattern.product.tag',
        string='Product Tags'
    )
    customer_part_id = fields.Char(string='Customer Part Number')
    date = fields.Date(
        string='Registration Date',
        default=fields.Datetime.now(),
        required=True
    )
    date_due = fields.Date(
        string='Review Date',
        compute='_compute_validity'
    )
    provider_id = fields.Many2one(
        comodel_name='res.partner',
        string='Provider'
    )
    owner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Model Owner'
    )
    model_category = fields.Many2one(
        'pattern.category',
        string='Material',
        help='Model making material',
        required=True
    )
    location = fields.Selection(
        [
            ('warehouse', 'Warehouse'),
            ('production', 'Production'),
            ('provider', 'Proveedor')
        ],
        string='Location',
        default='warehouse',
        required=True
    )
    location_detail = fields.Char(string='Location detail')
    quantity = fields.Text(string='Hearts quantity')
    model_capacity = fields.Selection(
        [
            ('rough', 'Rough'),
            ('normal', 'Normal'),
            ('light', 'Light')
        ], 
        string='Type of use',
        default='normal',
        required=True
    )
    base = fields.Float(string='Base')
    height = fields.Float(string='Height')
    width = fields.Float(string='Width')
    model_uom_id = fields.Many2one(
        'uom.uom',
        string='UOM Model',
        help='Unit of measurement',
        required=True
    )
    component_cant = fields.Integer(
        string='Components quantity',
        help='Components quantity feeding systems'
    )
    review_id = fields.One2many(
        comodel_name='pattern.review',
        inverse_name='pattern_id',
        string='Reviews'
    )
    is_extern = fields.Boolean(string='Extern')
    files_review = fields.One2many(
        comodel_name='pattern.files',
        inverse_name='pattern_id',
        string='Files review'
    )
    repairs = fields.One2many(
        comodel_name='pattern.repairs',
        inverse_name='pattern_id',
        string='Repairs'
    )
    description = fields.Text(string='Description')
    release = fields.Boolean(
        string='Release',
        readonly=True
    )
    release_user = fields.Many2one(
        'res.users',
        string="Release user",
		readonly=True
    )
    release_date = fields.Datetime(
        string='Release date',
        readonly=True
    )
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('optimum', 'Optimum'),
            ('acceptable', 'Acceptable'),
            ('deteriorated', 'Deteriorated'),
            ('repair', 'Repair'),
        ],
        string='Model condition',
        required=True, readonly=True, copy=False, tracking=True,
        default='draft'
    )
    active = fields.Boolean(
        'Active',
        default=True
    )
    validity = fields.Float(
        string='Days of life',
        compute='_compute_review_days'
    )
    pattern_status = fields.Char(
        string='Last review',
        compute='_compute_review_id'
    )

    @api.depends('validity')
    def _compute_validity(self):
        for pattern in self:
            review_days = timedelta(days=pattern.validity)
            pattern.date_due = pattern.date + review_days
    
    @api.depends('product_id')
    def _compute_patter_name(self):
        self.name = ''
        for data_model in self:
            data_model.name = self.product_id.name

    @api.depends('model_category')
    def _compute_review_days(self):  
        self.validity = 0 
        for data_model in self:
            data_model.validity = self.model_category.revision_time

    @api.depends('review_id')
    def _compute_review_id(self):
        review = self.env['pattern.review'].search(
            [('pattern_id', '=', self.id)], order='create_date desc', limit=1) 
        self.pattern_status = review.result

    def button_release(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Change state model',
            'view_mode': 'form',
            'res_model': 'wizard.pattern.state',
            'target': 'new',
            'context': {
                'default_pattern_id': self.id,
                },
        }
    
    def button_repair(self):
        print()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Repair model',
            'view_mode': 'form',
            'res_model': 'pattern.repairs',
            'target': 'new',
            'context': {
                'default_pattern_id': self.id,
                },
        }

    @api.model
    def create(self, vals):
        new_pattern = super().create(vals)
        new_pattern.state = 'optimum'
        return new_pattern

    @api.model
    def _cron_pattern_state_validation(self):
        pattern_ids = self.search([])
        for pattern in pattern_ids:
            if pattern.review_id:
                pattern.state = pattern.review_id[-1].result
                if pattern.review_id[-1].result == 'deteriorated':
                    pattern.release = False
                
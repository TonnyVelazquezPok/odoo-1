# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.AbstractModel):
    _inherit = 'product.template'

    mold_qty = fields.Float(
        string='Quantity per mold',
    )
    injection_qty = fields.Float(
        string='Amount per injection'
    )
    gross_weight = fields.Float(
        string="Gross weight"
    )
    casting_weight = fields.Float(
        string="Casting weight"
    )
    part_weight = fields.Float(
        string="Part weight"
    )
    pwm = fields.Float(
        string="PWM"
    )
    shipping_weight = fields.Float(
        string="Shipping weight"
    )
    mould_type = fields.Selection(
        [
            ("ceramic molding", "Ceramic molding"),
            ("sand molding", "Sand molding"),
            ("n/a", "N/A")
        ],
        string="Mould type"
    )
    gross_yield = fields.Float(
        string="Gross yield",
        compute='_compute_get_gross_yield'
    )
    casting_yield = fields.Float(
        string="Casting yield",
        compute='_compute_get_casting_yield'
    )
    total_yield = fields.Float(
        string="Total yield",
        compute='_compute_get_total_yield'
    )
    red_equ = fields.Char(
        string='RED EQ',
        size=50
    )
    avr = fields.Char(
        string='AVR',
        size=50
    )
    smr = fields.Char(
        string='SMR',
        size=50
    )
    cmr = fields.Char(
        string='CMR',
        size=50
    )
    coupon = fields.Char(
        string='Coupon',
        size=50
    )
    product_customer_id = fields.One2many(
        comodel_name='product.customer',
        inverse_name='product_template_id',
        string='Customer Products'
    )
    welding_documents =fields.One2many(
        comodel_name='product.welding.specification.document',
        inverse_name='product_template_id',
        string='Welding documents files'
    )
    external_specification =fields.Many2one(
        'quality.specification',
        string='External Specification'
    )
    internal_specification =fields.Many2one(
        'quality.specification',
        string='Internal Specification'
    )
    drawing_files = fields.One2many(
        comodel_name='product.issues',
        inverse_name='product_template_id',
        string='Drawing files'
    )
    product_certifications = fields.One2many(
        comodel_name='product.cert',
        inverse_name='product_template_id',
        string='Product Certification'
    )
    product_mrp = fields.One2many(
        comodel_name='mrp.bom',
        inverse_name='product_tmpl_id',
        string='Product bom'
    )

    @api.depends('casting_weight', 'gross_weight')
    def _compute_get_gross_yield(self):
        for product in self:
            product.gross_yield = (product.casting_weight / product.gross_weight)*100

    @api.depends('part_weight', 'gross_weight')
    def _compute_get_casting_yield(self):
        for product in self:
            product.casting_yield = (product.part_weight / product.gross_weight)*100

    @api.depends('part_weight', 'gross_weight')
    def _compute_get_total_yield(self):
        for product in self:
            product.total_yield = (product.part_weight / product.gross_weight)*100
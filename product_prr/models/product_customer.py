from odoo import models, fields, api

class ProductCustomer(models.Model):
    _name = 'product.customer'
    _description = 'Products from customers'

    part_number = fields.Char(
        size=50,
        string='Part Number',
    )
    customers = fields.Many2many(
        comodel_name='res.partner',
        string="Customers",
    )
    product_template_id = fields.Many2one(
        comodel_name='product.template',
        string='Product'
    )
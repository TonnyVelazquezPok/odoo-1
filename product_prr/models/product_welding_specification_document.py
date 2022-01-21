from odoo import models, fields, api

class ProductWeldingSpecificationDocument(models.Model):
    _name = 'product.welding.specification.document'
    _description = 'Welding Procedure Specification Documents'

    name = fields.Char(
        string='Name',
        size=50,
    )
    notes = fields.Text(
        string="Notes",
    )
    description = fields.Text(
        string="Description",
    )
    document_file = fields.Many2many(
        'ir.attachment',
        string="Document file",
        help='You can attach the copy of your Letter'
    )
    product_template_id = fields.Many2one(
        comodel_name='product.template',
        string='Product'
    )
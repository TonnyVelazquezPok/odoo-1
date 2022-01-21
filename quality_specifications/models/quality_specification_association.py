from odoo import fields, models


class QualitySpecificationAssociation(models.Model):
    _name = "quality.specification.association"
    _description = "Quality Specification Association"
    _order = 'sequence'

    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product'
    )
    customer_id = fields.Many2one(
        comodel_name='res.partner',
        string='Customer'
    )
    sequence = fields.Integer(string='Sequence')
    specification_id = fields.Many2one(
        'quality.specification',
        string='Specification',
        index=True,
        ondelete='cascade',
        required=True
    )
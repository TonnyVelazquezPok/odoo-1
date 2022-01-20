from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    product_issue_id = fields.One2many(
        comodel_name='product.issues',
        inverse_name='drawing_owner',
        string='Issue Products',
    )

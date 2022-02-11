from odoo import models, fields, api

class QualitySpecification(models.Model):
    _inherit = "quality.specification"

    product_templates_external = fields.One2many(
        string="Product Templates external",
        comodel_name="product.template",
        inverse_name="external_specification"
    )
    product_templates_internal = fields.One2many(
        string="Product Templates internal",
        comodel_name="product.template",
        inverse_name="internal_specification"
    )
    cert_specification = fields.One2many(
        string="Certification specification",
        comodel_name="product.cert",
        inverse_name="specification"
    )
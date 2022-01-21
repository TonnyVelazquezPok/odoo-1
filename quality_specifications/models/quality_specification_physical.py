from odoo import fields, models


class QualitySpecificationPhysical(models.Model):
    _name = "quality.specification.physical"
    _description = "Quality Specification Physical"
    _order = 'sequence'

    name = fields.Char(
        'Test',
        required=True
    )
    uom_id = fields.Many2one(
        'uom.uom',
        'Unit of Measure',
        required=True
    )
    minimum = fields.Float(
        'Minimum',
        digits='Specification Physical'
    )
    maximum = fields.Float(
        'Maximum',
        digits='Specification Physical'
    )
    sequence = fields.Integer('Sequence')
    specification_id = fields.Many2one(
        'quality.specification',
        string='Specification',
        index=True,
        ondelete='cascade',
        required=True
    )

    _sql_constraints = [
        ('spec_name_uniq',
            'unique (specification_id,name)',
            'Duplicate physical tests in specification not allowed !')
    ]

from odoo import fields, models


class QualitySpecificationChemical(models.Model):
    _name = "quality.specification.chemical"
    _description = "Quality Specification Chemical"
    _order = 'sequence'

    name = fields.Char(
        'Test',
        required=True
    )
    element_id = fields.Many2one(
        'quality.chemical.element',
        'Element'
    )
    formula_id = fields.Many2one(
        'quality.formula',
        'Formula'
    )
    minimum = fields.Float(
        'Minimum',
        digits='Specification Chemical'
    )
    maximum = fields.Float(
        'Maximum',
        digits='Specification Chemical'
    )
    internal_minimum = fields.Float(
        'Internal minimum',
        digits='Specification Chemical'
    )
    internal_maximum = fields.Float(
        'Internal maximum',
        digits='Specification Chemical'
    )
    sequence = fields.Integer(string='Sequence')
    combination = fields.Boolean(string='Combination')
    specification_id = fields.Many2one(
        'quality.specification',
        string='Specification',
        index=True,
        ondelete='cascade',
        required=True
    )

    _sql_constraints = [
        ('spec_element_uniq',
            'unique (specification_id,element_id)',
            'Duplicate elements in specification not allowed !')
    ]

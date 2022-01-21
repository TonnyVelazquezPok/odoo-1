from odoo import fields, models


class QualitySpecificationParameter(models.Model):
    _name = "quality.specification.parameter"
    _description = "Quality Specification Parameters"
    _order = 'sequence'

    name = fields.Char(
        string='Parameter'
    )
    sequence = fields.Integer('Sequence')
    uom_id = fields.Many2one(
        'uom.uom',
        'UOM',
        required=True
    )
    minimum = fields.Float(
        'Minimum',
        digits='Specification Parameter'
    )
    maximum = fields.Float(
        'Maximum',
        digits='Specification Parameter'
    )
    grade = fields.Float(
        'Grade'
    )
    set_point = fields.Float(
        'Set Point'
    )
    specification_id = fields.Many2one(
        'quality.specification',
        string='Specification',
        index=True,
        ondelete='cascade',
        required=True
    )
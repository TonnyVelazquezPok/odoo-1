from odoo import fields, models


class QualitySpecification(models.Model):
    _name = "quality.specification"
    _description = "Quality Specification"
    _order = 'name'

    name = fields.Char(
        'Specification',
        required=True
    )
    description = fields.Text('Description')
    notes = fields.Text('Notes')
    balance_element_id = fields.Many2one(
        'quality.chemical.element',
        string='Balance Element'
    )
    minimum = fields.Float(
        'Minimum',
        digits='Specification Chemical'
    )
    maximum = fields.Float(
        'Maximum',
        digits='Specification Chemical'
    )
    non_defined = fields.Float(
        'Non Defined Element',
        digits='Non Defined Element'
    )
    nde_max = fields.Float(
        'NDE Max',
        digits='NDE Max'
    )
    specification_physical_ids = fields.One2many(
        string="Physical Tests",
        comodel_name="quality.specification.physical",
        inverse_name="specification_id"
    )
    specification_chemical_ids = fields.One2many(
        string="Chemical Tests",
        comodel_name="quality.specification.chemical",
        inverse_name="specification_id"
    )
    specification_association_ids = fields.One2many(
        string="Chemical Association",
        comodel_name="quality.specification.association",
        inverse_name="specification_id"
    )
    specification_file_ids = fields.One2many(
        string="Chemical Files",
        comodel_name="quality.specification.file",
        inverse_name="specification_id"
    )
    specification_parameter_ids = fields.One2many(
        string="Chemical Parameters",
        comodel_name="quality.specification.parameter",
        inverse_name="specification_id"
    )
    active = fields.Boolean(
        'Active',
        default=True,
        help="If unchecked, it will allow you to hide the specification "
        "without removing it."
    )

    _sql_constraints = [
        (
            'name',
            'UNIQUE(name)',
            'There exist an specification with the selected name'
        )
    ]

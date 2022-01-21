from odoo import models, fields


class QualityChemicalElement(models.Model):
    _name = 'quality.chemical.element'
    _description = 'Chemical Element'

    name = fields.Char(string="Element", required=True, translate=True)
    symbol = fields.Char(index=True, required=True)
    number = fields.Integer(string="Atomic number", required=True)

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)',
            'You can not have two elements with the same name !'),
        ('symbol_uniq', 'UNIQUE(symbol)',
            'You can not have two elements with the same symbol !'),
        ('number_uniq', 'UNIQUE(number)',
            'You can not have two elements with the same number !')
    ]

from odoo import fields, models


class QualitySpecificationFile(models.Model):
    _name = "quality.specification.file"
    _description = "Quality Specification Files"
    _order = 'name'

    name = fields.Char(
        string='Document Name'
    )
    notes = fields.Text(
        string='Notes'
    )
    file = fields.Binary("File")
    file_name = fields.Char(string='File Name') 
    specification_id = fields.Many2one(
        'quality.specification',
        string='Specification',
        index=True,
        ondelete='cascade',
        required=True
    )
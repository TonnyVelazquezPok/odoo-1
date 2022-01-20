from odoo import fields, models, api


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    name = fields.Char(
        string='Name'
    )
    default = fields.Boolean(
        strong='Default',
        default=False,
    )
    default_name = fields.Char(
        string='Name',
        compute='_compute_get_default_name',
    )

    @api.depends('name')
    def _compute_get_default_name(self):
        for mrp_bom in self:
            if mrp_bom.default is True:
                mrp_bom.default_name = "Default"
            else:
                mrp_bom.default_name = ""

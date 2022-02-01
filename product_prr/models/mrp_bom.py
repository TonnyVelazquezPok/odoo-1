from odoo import fields, models, api


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    name = fields.Char(
        string='Name'
    )
    default = fields.Boolean(
        string='Default',
        default=False
    )
    default_name = fields.Char(
        string='Name',
        compute='_compute_get_default_name'
    )
    time_cycle_manual_total = fields.Float(
        'Total ',
        compute="_compute_get_total_time_cycle_manual"
    )

    @api.depends('operation_ids')
    def _compute_get_total_time_cycle_manual(self):
        for mrp in self:
            for operation in mrp.operation_ids:
                mrp.time_cycle_manual_total += operation.time_cycle_manual

    @api.depends('name')
    def _compute_get_default_name(self):
        for mrp_bom in self:
            if mrp_bom.default is True:
                mrp_bom.default_name = "Default"
            else:
                mrp_bom.default_name = ""

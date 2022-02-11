from odoo import fields, models, api


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    default = fields.Boolean(
        string='Default',
        default=False
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


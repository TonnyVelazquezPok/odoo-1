from odoo import models, fields, api

class MrpRoutingWorkcenter(models.Model):
    _inherit = 'mrp.routing.workcenter'

    process_notes = fields.Text(
        string='Procces notes'
    )
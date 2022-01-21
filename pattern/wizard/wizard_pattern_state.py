# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta


class WizardPatternState(models.TransientModel):
	_name = 'wizard.pattern.state'
	_description = 'Wizard state model'

	pattern_id = fields.Many2one(
		'pattern',
		string='Model'
	)
	release_user = fields.Many2one(
        "res.users",
        string="User",
        default=lambda self: self.env.user,
		readonly=True
    )
	release_date = fields.Datetime(
		string='Release date',
		readonly=True,
		default=fields.Datetime.now()
		)
	state = fields.Selection(
        selection=[
        	('optimum', 'Optimum'),
            ('acceptable', 'Acceptable'),
            ('deteriorated', 'Deteriorated'),
        ],
        string='Model condition',
		required=True
    )
	location = fields.Selection(
        [
            ('warehouse', 'Warehouse'),
            ('production', 'Production'),
            ('provider', 'Proveedor')
        ],
        string='Location',
        required=True
    )
	location_detail = fields.Char(
        string='Location Detail'
    )

	def button_add_release(self):
		self.pattern_id.release_user = self.release_user
		self.pattern_id.release_date = self.release_date
		self.pattern_id.state = self.state
		if self.state == 'deteriorated':
			self.pattern_id.release = False
		else:
			self.pattern_id.release = True
		self.pattern_id.location = self.location
		self.pattern_id.location_detail = self.location_detail
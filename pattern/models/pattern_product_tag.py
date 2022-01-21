# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PatternProductTag(models.Model):
	_name = 'pattern.product.tag'
	_description = 'Tags Product - Model'
	_sql_constraints = [
		('name_unique', 'UNIQUE(name)', "This tag already exist!")
	]

	name = fields.Char(
		string='Tag',
		size=64,
		required=True
	)

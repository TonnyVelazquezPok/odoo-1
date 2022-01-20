# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductIssues(models.Model):
    _name = 'product.issues'
    _description = 'Container of the UIDs to work'

    product_template_id = fields.Many2one(
        comodel_name='product.template',
        string='Product'
    )
    drawing_owner = fields.Many2one(
        comodel_name='res.partner',
        string='Drawing owner',
    )
    drawing_number = fields.Char(
        size=50,
        string='Drawing number',
    )
    drawing_review = fields.Char(
        size=50,
        string='Drawing review',
    )
    drawing_date_revision = fields.Datetime(
        size=50,
        string='Drawing date revision',
    )
    drawing_file = fields.Many2many(
        'ir.attachment',
        string="Attachment",
        help='You can attach the copy of your Letter'
    )
    see_production = fields.Selection(
        [
            ('yes', 'Yes'),
            ('no', 'No'),
        ],
        string="See production?",
    )
    drawing_type = fields.Selection(
        [
            ('AC - Areas criticas','AC - Areas criticas'),
            ('AM - Armado del molde','AM - Armado del molde'),
            ('AV - Corte de pieza','AV - Corte de pieza'),
            ('AV - Corte de recargue','AV - Corte de recargue'),
            ('AV - Criterios de aceptación','AV - Criterios de aceptación'),
            ('AV - Desmoldeo','AV - Desmoldeo'),
            ('AV - Detallado','AV - Detallado'),
            ('AV - Detallado radios','AV - Detallado radios'),
            ('AV - Dureza','AV - Dureza'),
            ('AV - Estampado','AV - Estampado'),
            ('AV - Grapas ceramicas','AV - Grapas ceramicas'),
            ('AV - Inyección de cera','AV - Inyección de cera'),
            ('AV - Marcaje','AV - Marcaje'),
            ('AV - Moldeo','AV - Moldeo'),
            ('AV - Pulido','AV - Pulido'),
            ('AV - Soldadura','AV - Soldadura'),
            ('AVC - Corte recargue','AVC - Corte recargue'),
            ('AVM - Marcaje','AVM - Marcaje'),
            ('AVM - Marcaje','AVM - Marcaje'),
            ('AVME - Medición','AVME - Medición'),
            ('AVT - Tensor','AVT - Tensor'),
            ('AVTT - ayuda visual de Tratamiento Térmico','AVTT - ayuda visual de Tratamiento Térmico'),
            ('BA - Baloneado','BA - Baloneado'),
            ('BOM - Bill of Materials','BOM - Bill of Materials'),
            ('CA - Criterios de Aceptación','CA - Criterios de Aceptación'),
            ('CA - Criterios de Aceptación PND','CA - Criterios de Aceptación PND'),
            ('Cl- Checklist','Cl- Checklist'),
            ('CM - Control de matrices','CM - Control de matrices'),
            ('CM - Control de modelos','CM - Control de modelos'),
            ('CPR - Control Pesos y Relaciones','CPR - Control Pesos y Relaciones'),
            ('Curso POK','Curso POK'),
            ('DI - Dibujo Inspección','DI - Dibujo Inspección'),
            ('DP - Dibujo Pintura','DP - Dibujo Pintura'),
            ('ED - Solido','ED - Solido'),
            ('EN - Ensamble','EN - Ensamble'),
            ('EN - Ensamble Cliente','EN - Ensamble Cliente'),
            ('FC - Fundición Cliente','FC - Fundición Cliente'),
            ('FM - Maquinado Final','FM - Maquinado Final'),
            ('Forging','Forging'),
            ('FP - Fundición POK','FP - Fundición POK'),
            ('MC - Maquinado Cliente','MC - Maquinado Cliente'),
            ('MF - Maquinado Final','MF - Maquinado Final'),
            ('MO - Modelo','MO - Modelo'),
            ('PDF- Solido','PDF- Solido'),
            ('PM - Plan de Manufactura','PM - Plan de Manufactura'),
            ('PM - Pre-maquinado','PM - Pre-maquinado'),
            ('Pre-forma Placa','Pre-forma Placa'),
            ('Pre-maquinado','Pre-maquinado'),
            ('QP - Quality Plan','QP - Quality Plan'),
            ('RC - Recubrimiento Cliente','RC - Recubrimiento Cliente'),
            ('RF - Reporte de Fusion','RF - Reporte de Fusion'),
            ('RT - Radiografia','RT - Radiografia'),
            ('SI - Sobre-imposición','SI - Sobre-imposición'),
            ('SO - Solido','SO - Solido'),
            ('SP - MT Cabezas','SP - MT Cabezas'),
            ('SP - MT Cables','SP - MT Cables'),
            ('SP - UT','SP - UT'),
            ('SV - Sistema de Vaciado','SV - Sistema de Vaciado'),
            ('SW - Solido','SW - Solido'),
            ('WTR- Wall Thickness Report','WTR- Wall Thickness Report'),
        ],
        string='Drawing type',
    )
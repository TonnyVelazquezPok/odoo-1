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
            ('ac_areas_criticas','AC - Areas criticas'),
            ('am_armado_molde','AM - Armado del molde'),
            ('av_corte_pieza','AV - Corte de pieza'),
            ('av_corte_recargue','AV - Corte de recargue'),
            ('av_criterios_aceptacion','AV - Criterios de aceptación'),
            ('av_desmoldeo','AV - Desmoldeo'),
            ('av_detallado','AV - Detallado'),
            ('av_detallado_radios','AV - Detallado radios'),
            ('av_dureza','AV - Dureza'),
            ('av_estampado','AV - Estampado'),
            ('av_grapas_ceramicas','AV - Grapas ceramicas'),
            ('av_inyeccion_cera','AV - Inyección de cera'),
            ('av_marcaje','AV - Marcaje'),
            ('av_moldeo','AV - Moldeo'),
            ('av_pulido','AV - Pulido'),
            ('av_soldadura','AV - Soldadura'),
            ('avc_corte_recargue','AVC - Corte recargue'),
            ('avn_marcaje','AVM - Marcaje'),
            ('avn_marcaje','AVM - Marcaje'),
            ('avme_medición','AVME - Medición'),
            ('avt_tensor','AVT - Tensor'),
            ('avtt_ayuda_visual_tratamiento_térmico','AVTT - ayuda visual de Tratamiento Térmico'),
            ('ba_baloneado','BA - Baloneado'),
            ('bom_bill_materials','BOM - Bill of Materials'),
            ('ca_criterios_aceptación','CA - Criterios de Aceptación'),
            ('ca_criterios_aceptación_pnd','CA - Criterios de Aceptación PND'),
            ('cl_checklist','Cl- Checklist'),
            ('cm_control_matrices','CM - Control de matrices'),
            ('cm_control_modelos','CM - Control de modelos'),
            ('cpr_control_pesos_relaciones','CPR - Control Pesos y Relaciones'),
            ('curso_pok','Curso POK'),
            ('di_dibujo_inspección','DI - Dibujo Inspección'),
            ('dp_dibujo_pintura','DP - Dibujo Pintura'),
            ('eD_solido','ED - Solido'),
            ('eN_ensamble','EN - Ensamble'),
            ('eN_ensamble_cliente','EN - Ensamble Cliente'),
            ('fC_fundición_cliente','FC - Fundición Cliente'),
            ('fM_maquinado_final','FM - Maquinado Final'),
            ('forging','Forging'),
            ('fp_fundición_pok','FP - Fundición POK'),
            ('ma_maquinado_cliente','MC - Maquinado Cliente'),
            ('mf_maquinado_final','MF - Maquinado Final'),
            ('mo_modelo','MO - Modelo'),
            ('pdf_solido','PDF- Solido'),
            ('pm_plan_manufactura','PM - Plan de Manufactura'),
            ('pm_pre-maquinado','PM - Pre-maquinado'),
            ('pre-forma_placa','Pre-forma Placa'),
            ('pre-maquinado','Pre-maquinado'),
            ('ap_quality_plan','QP - Quality Plan'),
            ('rc_recubrimiento_cliente','RC - Recubrimiento Cliente'),
            ('rf_reporte_fusion','RF - Reporte de Fusion'),
            ('rt_radiografia','RT - Radiografia'),
            ('si_sobre-imposición','SI - Sobre-imposición'),
            ('so_solido','SO - Solido'),
            ('sp_mt_cabezas','SP - MT Cabezas'),
            ('sp_mt_cables','SP - MT Cables'),
            ('sp_ut','SP - UT'),
            ('sv_sistema_vaciado','SV - Sistema de Vaciado'),
            ('sw_solido','SW - Solido'),
            ('wtr_wall_thickness_report','WTR- Wall Thickness Report'),
        ],
        string='Drawing type',
    )
from odoo import models, fields, api

class ProductCert(models.Model):
    _name = 'product.cert'
    _description = 'Product certification'

    specification =fields.Many2one(
        'quality.specification',
        string='Specification',
    )
    scan_plan = fields.Char(
        string='Scan plan',
        size=50,
    )
    draw_area = fields.Char(
        string='Draw area',
        size=50,
    )
    certification_type = fields.Char(
        string='Certification type',
        compute='_compute_get_type'
    )
    product_template_id = fields.Many2one(
        comodel_name='product.template',
        string='Product'
    )
    certifications_files = fields.Many2many(
        'ir.attachment',
        string="Attachment",
        help='You can attach the copy of your Letter'
    )
    statement_mtr = fields.Boolean(
        strong='Statement on MTR',
        default=False,
    )
    table_chart_image_mtr = fields.Boolean(
        strong='Table/Chart/Image on MTR',
        default=False,
    )
    pok_format = fields.Boolean(
        strong='Individual Report (POK format)',
        default=False,
    )
    customer_format = fields.Boolean(
        strong='Individual Report (Customer format)',
        default=False,
    )
    name = fields.Selection(
        [
            ('05_chemical', '05 - Chemical Analysis'),
            ('07_quality', '07 - Quality Test Cupon'),
            ('10_tension', '10 - Tension Properties'),
            ('15_impact', '15 - Impact Properties'),
            ('20_hardness', '20 - Hardness Testing'),
            ('23_heat_cycle', '23 - Heat Treat Cycle'),
            ('25_heat_charts', '25 - Heat Treat Charts'),
            ('30_metallograpich', '30 - Metallographic Examination'),
            ('35_visual', '35 - Visual Test'),
            ('40_penetrant', '40 - Penetrant Test'),
            ('45_magnetic', '45 - Magnetic Test'),
            ('50_ultrasonic', '50 - Ultrasonic Test'),
            ('53_volumetric_destructive', '53 - Volumetric Destructive Test'),
            ('55_radiographic', '55 - Radiographic Test'),
            ('57_volumetric_nde', '57 - Volumetric Summary NDE'),
            ('60_dimensional', '60 - Dimensional Verification'),
            ('65_lot', '65 - Lot Number'),
            ('66_ped', '66 - PED 2014/68/EU'),
            ('67_certificate', '67 - Certificate of Conformity'),
            ('68_deviation', '68 - Request for Deviation'),
            ('69_mr0175', '69 - NACE MR0175'),
            ('70_hardsurfaced', '70 - Hardsurfaced'),
            ('75_surface_treat', '75 - Surface Treat'),
            ('76_surface_coating', '76 - Surface Coating'),
            ('77_weigth', '77 - Weigth'),
            ('78_traceability', '78 - Traceability Marking'),
            ('83_welding', '83 - Welding Repair'),
            ('99_shipment', '99 - Verify Before Shipment'),
        ],
        string='Certification',
    )
    type = fields.Selection(
        [
            ('Ensamble', 'Ensamble'),
            ('Ensamble_found', 'Ensamble (Fund)'),
            ('fund_maq', 'Fund. & Maq.'),
            ('fund_Cliente', 'Fund. Cliente'),
            ('fund_pa_ps', 'Fund. PA. PS.'),
            ('fundición', 'Fundición'),
            ('fund_pa', 'Fund. & PA'),
            ('lote_pa', 'Lote de PA'),
            ('maquinado', 'Maquinado'),
            ('maq_pa', 'Maq. & PA'),
            ('modelo', 'Modelo'),
            ('n/a', 'N/A'),
            ('pa_fund.', 'PA - Fund.'),
            ('pa_modelo', 'PA - Modelo'),
            ('pa_pz_sacrificio', 'PA - Pz Sacrificio'),
            ('solo_pa', 'Solo PA'),
            ('solo_pa_fund.', 'Solo PA Fund.'),
        ],
        string='Product Type',
    )
    sample_size = fields.Selection(
        [
            ('8%', '8%'),
            ('10%', '10%'),
            ('100%', '100%'),
            ('1_cada_10', '1 cada 10'),
            ('1_cada_10_cada_colada', '1 cada 10 cada Colada'),
            ('1_cada_12', '1 cada 12'),
            ('1_cada_15', '1 cada 15'),
            ('1_cada árbol', '1 cada árbol'),
            ('1_por colada', '1 por colada'),
            ('1_por colada maestra', '1 por colada maestra'),
            ('1_por_día', '1 por día'),
            ('1_por_lote_tt', '1 por lote TT'),
            ('1_por_lote_tt_de_colada', '1 por lote TT de colada'),
            ('1_por_lote_tt_por_colada', '1 por lote TT por colada'),
            ('1_por_pedido', '1 por Pedido'),
            ('1_por_pieza', '1 por pieza'),
            ('1_pz_cada_6_meses', '1 pz cada 6 meses'),
            ('10%_min_3', '10%, min 3'),
            ('100_in_critical_zones', '100% in Critical Zones'),
            ('100%_of_casting_surfaces', '100% of Casting Surfaces'),
            ('100%_segun_sp_ut', '100% segun SP-UT'),
            ('100%_only_in_ut_zone', '100%, Only in UT Zone'),
            ('eventual', 'Eventual'),
            ('level_ii, AQL 1.5', 'Level II, AQL 1.5'),
            ('lote_pa', 'Lote de PA'),
            ('nivel_ii_con_1.5_aql', 'Nivel II con 1.5 AQL'),
            ('nivel_ii_con_4.0_aql', 'Nivel II con 4.0 AQL'),
            ('pa_pieza_sacrificio', 'PA Pieza Sacrificio'),
            ('pndg', 'PNDG'),
            ('por_envio', 'Por Envio'),
            ('pre-machining_zone_only', 'Pre-machining zone only'),
            ('segun_po', 'Segun PO'),
            ('segun_vol. NDE', 'Segun Vol. NDE'),
            ('solo_pa', 'Solo PA'),
            ('solo_pa_fundicion', 'Solo PA Fundicion'),
        ],
        string='Sample size',
    )

    @api.depends('statement_mtr', 'table_chart_image_mtr', 'pok_format', 'customer_format')
    def _compute_get_type(self):
        for cert in self:
            if cert.statement_mtr is True and cert.table_chart_image_mtr is False and \
                cert.pok_format is False and cert.customer_format is False:

                cert.certification_type = 'En MTR'

            elif cert.statement_mtr is False and cert.table_chart_image_mtr is True and \
                cert.pok_format is False and cert.customer_format is False:

                cert.certification_type = 'Tabla, imagen o gráfico en MTR'

            elif cert.statement_mtr is False and cert.table_chart_image_mtr is False and \
                cert.pok_format is True and cert.customer_format is False:

                cert.certification_type = 'Certificado en formato POK'

            elif cert.statement_mtr is False and cert.table_chart_image_mtr is False and \
                cert.pok_format is False and cert.customer_format is True:

                cert.certification_type = 'Certificado en formato Cliente'

            elif cert.statement_mtr is True and cert.table_chart_image_mtr is True and \
                cert.pok_format is False and cert.customer_format is False:

                cert.certification_type = 'En MTR y Tabla, imagen o gráfico en MTR'

            elif cert.statement_mtr is True and cert.table_chart_image_mtr is False and \
                cert.pok_format is True and cert.customer_format is False:

                cert.certification_type = 'En MTR y Certificado en formato POK'

            elif cert.statement_mtr is True and cert.table_chart_image_mtr is False and \
                cert.pok_format is True and cert.customer_format is True:

                cert.certification_type = 'En MTR y Certificado en formato Cliente'

            else:

                cert.certification_type = 'Error; consultar con ingeniería'
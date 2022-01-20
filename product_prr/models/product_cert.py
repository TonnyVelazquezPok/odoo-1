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
        size=50,
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
    name = fields.Selection(
        [
            ('05 - Chemical Analysis', '05 - Chemical Analysis'),
            ('07 - Quality Test Cupon', '07 - Quality Test Cupon'),
            ('10 - Tension Properties', '10 - Tension Properties'),
            ('15 - Impact Properties', '15 - Impact Properties'),
            ('20 - Hardness Testing', '20 - Hardness Testing'),
            ('23 - Heat Treat Cycle', '23 - Heat Treat Cycle'),
            ('25 - Heat Treat Charts', '25 - Heat Treat Charts'),
            ('30 - Metallographic Examination', '30 - Metallographic Examination'),
            ('35 - Visual Test', '35 - Visual Test'),
            ('40 - Penetrant Test', '40 - Penetrant Test'),
            ('45 - Magnetic Test', '45 - Magnetic Test'),
            ('50 - Ultrasonic Test', '50 - Ultrasonic Test'),
            ('53 - Volumetric Destructive Test', '53 - Volumetric Destructive Test'),
            ('55 - Radiographic Test', '55 - Radiographic Test'),
            ('57 - Volumetric Summary NDE', '57 - Volumetric Summary NDE'),
            ('60 - Dimensional Verification', '60 - Dimensional Verification'),
            ('65 - Lot Number', '65 - Lot Number'),
            ('66 - PED 2014/68/EU', '66 - PED 2014/68/EU'),
            ('67 - Certificate of Conformity', '67 - Certificate of Conformity'),
            ('68 - Request for Deviation', '68 - Request for Deviation'),
            ('69 - NACE MR0175', '69 - NACE MR0175'),
            ('70 - Hardsurfaced', '70 - Hardsurfaced'),
            ('75 - Surface Treat', '75 - Surface Treat'),
            ('76 - Surface Coating', '76 - Surface Coating'),
            ('77 - Weigth', '77 - Weigth'),
            ('78 - Traceability Marking', '78 - Traceability Marking'),
            ('83 - Welding Repair', '83 - Welding Repair'),
            ('99 - Verify Before Shipment', '99 - Verify Before Shipment'),
        ],
        string='Certification',
    )
    type = fields.Selection(
        [
            ('Ensamble', 'Ensamble'),
            ('Ensamble (Fund)', 'Ensamble (Fund)'),
            ('Fund. & Maq.', 'Fund. & Maq.'),
            ('Fund. Cliente', 'Fund. Cliente'),
            ('Fund. PA. PS.', 'Fund. PA. PS.'),
            ('Fundición', 'Fundición'),
            ('Fund. & PA', 'Fund. & PA'),
            ('Lote de PA', 'Lote de PA'),
            ('Maquinado', 'Maquinado'),
            ('Maq. & PA', 'Maq. & PA'),
            ('Modelo', 'Modelo'),
            ('N/A', 'N/A'),
            ('PA - Fund.', 'PA - Fund.'),
            ('PA - Modelo', 'PA - Modelo'),
            ('PA - Pz Sacrificio', 'PA - Pz Sacrificio'),
            ('Solo PA', 'Solo PA'),
            ('Solo PA Fund.', 'Solo PA Fund.'),
        ],
        string='Product Type',
    )
    sample_size = fields.Selection(
        [
            ('8%', '8%'),
            ('10%', '10%'),
            ('100%', '100%'),
            ('1 cada 10', '1 cada 10'),
            ('1 cada 10 cada Colada', '1 cada 10 cada Colada'),
            ('1 cada 12', '1 cada 12'),
            ('1 cada 15', '1 cada 15'),
            ('1 cada árbol', '1 cada árbol'),
            ('1 por colada', '1 por colada'),
            ('1 por colada maestra', '1 por colada maestra'),
            ('1 por día', '1 por día'),
            ('1 por lote TT', '1 por lote TT'),
            ('1 por lote TT de colada', '1 por lote TT de colada'),
            ('1 por lote TT por colada', '1 por lote TT por colada'),
            ('1 por Pedido', '1 por Pedido'),
            ('1 por pieza', '1 por pieza'),
            ('1 pz cada 6 meses', '1 pz cada 6 meses'),
            ('10%, min 3', '10%, min 3'),
            ('100% in Critical Zones', '100% in Critical Zones'),
            ('100% of Casting Surfaces', '100% of Casting Surfaces'),
            ('100% segun SP-UT', '100% segun SP-UT'),
            ('100%, Only in UT Zone', '100%, Only in UT Zone'),
            ('Eventual', 'Eventual'),
            ('Level II, AQL 1.5', 'Level II, AQL 1.5'),
            ('Lote de PA', 'Lote de PA'),
            ('Nivel II con 1.5 AQL', 'Nivel II con 1.5 AQL'),
            ('Nivel II con 4.0 AQL', 'Nivel II con 4.0 AQL'),
            ('PA Pieza Sacrificio', 'PA Pieza Sacrificio'),
            ('PNDG', 'PNDG'),
            ('Por Envio', 'Por Envio'),
            ('Pre-machining zone only', 'Pre-machining zone only'),
            ('Segun PO', 'Segun PO'),
            ('Segun Vol. NDE', 'Segun Vol. NDE'),
            ('Solo PA', 'Solo PA'),
            ('Solo PA Fundicion', 'Solo PA Fundicion'),
        ],
        string='Sample size',
    )
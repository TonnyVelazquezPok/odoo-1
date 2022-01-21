# -*- coding: utf-8 -*-
{
    'name': "Quality Formula",
    'summary': "Quality Formula records",
    'description': """
        Long description of module's purpose
    """,
    'author': "Corporación POK S.A. de C.V.",
    'website': "https://pok.com.mx",
    'category': 'Quality',
    'version': '0.1',
    'depends': [
        'base',
        'quality_chemical_element'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/quality_formula_view.xml'
    ],
}

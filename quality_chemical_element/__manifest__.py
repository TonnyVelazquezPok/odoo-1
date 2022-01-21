{
    'name': "Quality Chemical Elements",
    'summary': """
        List of all chemical elements
    """,
    'author': "Corporación POK S.A. de C.V.,Odoo Community Association (OCA)",
    'website': "https://pok.com.mx",
    "license": "Other proprietary",
    'category': 'Quality',
    'version': '15.0.0.1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/quality_chemical_element_views.xml',
        # 'views/quality_chemical_element_menus.xml',
        'data/quality_element_data.xml'
    ],
}

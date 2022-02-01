# -*- coding: utf-8 -*-
{
    'name': "Model Control",

    'summary': """
        Module model control
        """,

    'description': """
        
    """,

    'author': "POK",
    'website': "https://www.pok.com.mx/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'product'],

    # always loaded
    'data': [
        'data/ir_cron_data.xml',
        'security/patern_groups.xml',
        'security/patern_security.xml',
        'security/ir.model.access.csv',
        'views/pattern_view.xml',
        'wizard/wizard_pattern_state.xml',
    ],
    'license': 'Other proprietary',
}

# -*- coding: utf-8 -*-
{
    'name': "Product Review Report",

    'summary': """
        Fields are added for the generation of the product review report to the product template
        """,

    'description': """
        Fields are added for the generation of the product review report to the product template
    """,

    "author": "Corporación POK S.A. de C.V.",
    "website": "https://pok.com.mx",
    'category': 'PRR',
    'version': '14.0.0.1.0',

    'depends': ['base', 'product', 'stock', "quality_chemical_element", "mrp", "quality_specifications"],

    'data': [
	    'security/product_prr_security.xml',
        'security/ir.model.access.csv',

        "views/product_view.xml",
        "views/product_mrp_bom_view.xml",
        "views/product_mrp_routing_workcenter_view.xml",
        "views/product_menu_views.xml",

        "report/product_prr_report.xml",
    ],
    'license': 'Other proprietary',
}

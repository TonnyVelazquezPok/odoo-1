# Copyright 2021 POK

{
    "name": "Quality Specifications",
    "version": "0.1",
    "description": """
        Quality specification
    """,
    "summary": "Quality specification records",
    "author": "Corporación POK S.A. de C.V.",
    "website": "https://pok.com.mx",
    "license": "Other proprietary",
    "category": "Quality",
    "depends": [
        "base",
        "product",
        "quality_chemical_element"
    ],
    "data": [
        'data/quality_specification_data.xml',
        'views/quality_specification_views.xml',
        'views/quality_specification_menus.xml',
        'security/ir.model.access.csv',
    ],
    "application": False,
    "installable": True,
}

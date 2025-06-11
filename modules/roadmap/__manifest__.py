# -*- coding: utf-8 -*-
{
    'name': "Event roadmap",

    'summary': "Create event roadmaps",

    'description': """
Long description of module's purpose
    """,

    'author': "Gori",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'event', 'Event extended', 'Artists', 'Event Scheedule'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/roadmap_report.xml',
        'views/roadmap_es.xml',
        'views/roadmap_cat.xml',
        'views/roadmap_en.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}


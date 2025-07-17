# -*- coding: utf-8 -*-
{
    'name': "Event Press Notes",

    'summary': "Add a unique press release for each event",

    'description': """
This module allows you to attach a press release to each event.

Features:
- Each event can have only one associated press note
- HTML fields for press note and press call content
- Support for attaching multiple images
- Clean separation from the core event module for better access control
    """,

    'author': "Gori",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'event'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/event_press_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}


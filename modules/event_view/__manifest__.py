# -*- coding: utf-8 -*-
{
    'name': "Event View",
    'summary': "Customize and enhance event view display on the website",
    'description': """
        This module customizes the presentation and structure of event-related views
        on the website, including the integration of images and additional event details.
        Requires the m2m_images module to manage optimized image handling.
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'event', 'm2m_images', 'website_event'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}


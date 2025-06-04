# -*- coding: utf-8 -*-
{
    'name': "m2m_images",

    'summary': "Many-to-Many Image Manager with Auto-Resizing",
    'description': """
Enhance your Odoo models with efficient many-to-many image management.

This module introduces a reusable model and image field logic to attach and manage multiple images per record, complete with automatic resizing (thumbnail, medium, and original). It's ideal for optimizing frontend performance and reducing bandwidth usage in web and mobile applications.

Key features:
- Define many-to-many image relationships for any model
- Automatic generation of thumbnail and medium-sized images
- Lightweight, frontend-optimized image delivery
- Extensible design for custom use cases
""",

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

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


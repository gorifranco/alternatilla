# -*- coding: utf-8 -*-
{
    'name': "Event extended",
    'summary': "Extiende eventos con hotel, horarios, promotor y enlace a entradas",
    'description': """
        Este módulo amplía los eventos de Odoo añadiendo información adicional útil para la gestión y visualización web del evento:
        - Hotel y comentarios de alojamiento
        - Promotor del evento
        - Enlace externo para la venta de entradas
        - Mejoras para la publicación web del evento
    """,

    'author': "Gori",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'event', 'mail', 'website_event'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/festival_views.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}


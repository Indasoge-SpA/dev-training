# -*- coding: utf-8 -*-
{
    'name': "exploration",

    "summary": """ Spaceships for Space Exploration""",
    "description": """
    
    Space Exploration spaceships
    
    """,

    'author': "Odoo SpA",
    'website': "http://www.indasoge.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Exploration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/spaceship_groups.xml',
        'security/spaceship_security.xml',
        'security/ir.model.access.csv',
        'views/spaceship_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/spaceship_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

# -*- coding: utf-8 -*-
# Odoo Basic Training

{
    "name": 'Mision lunar',
    "summary": """ Misión espacial para poblar la luna""",
    "description": """
    
    Misión espacial, módulo logístico
    
    """,
    
    "author": 'Indasoge SpA',
    "website": 'https://www.indasoge.com',
    
    "category": 'Training',
    
    "version": '0.1',
    
    "depends": ['base'],
    
    "data": [
        'security/mision_lunar_security.xml',
        'security/ir.model.access.csv',
    ],
    
    "demo": [
        'demo/mision_lunar_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
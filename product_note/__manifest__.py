# -*- coding: utf-8 -*-

{
    'name': 'Product Notes',
    'version': '18.0.1.0.0',
    'summary': 'Allows users to add specific notes to products.',
    'author': 'Your Name',
    'category': 'Sales/Sales',
    'depends': ['base', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_note_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
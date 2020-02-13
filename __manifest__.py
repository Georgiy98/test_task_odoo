# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Test App',
    'version': '1.0',
    'category': 'Test category',
    'description': "",
    'depends': [],
    'data': ['views/test_product.xml',
             'views/test_category.xml',
             'views/test_subcategory.xml',
             'views/test_group.xml',
             'security/ir.model.access.csv',
             ],
    'installable': True,
    'application': True,
}

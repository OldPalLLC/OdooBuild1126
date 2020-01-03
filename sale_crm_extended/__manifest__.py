# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Sale Crm Extended",
    'version': '1.0',
    'depends': ['sale_crm'],
    'author': 'Odoo Inc',
    'maintainer': 'Odoo Inc',
    'category': 'Sales',
    'description': """
Sale Crm Extended
=================
TASK ID: 2154872
- Hide the 'Confirm' button on quotation if the user is came to the quotation from CRM app.
    """,
    # data files always loaded at installation
    'data': [
        'views/sale_crm_views.xml',
    ],
}
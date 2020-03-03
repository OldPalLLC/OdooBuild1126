# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "auto_lot_info",
    'version': '1.1',
    'depends': ['mrp'],
    'license': 'LGPL-3',
    'author': 'Odoo Inc',
    'maintainer': 'Odoo Inc',
    'category': 'Manufacturing',
    'description': """
Stock Production Lot Extended
=================
TASK ID: 2194700
1. Create five new fields on the Lot form view under the model stock.production.lot

1.1 Many to One field that says "Produced From" by selecting the model "stock.production.lot ". This field should always be editable so that if the client wants, they should be able to change the Lot# from the drop-down list

1.2 Two decimal fields: THC precent and CBD percent

1.3 One text field: Lab Name

1.4 One selection filed: Test Results with values as Pass and Fail

2. Manufacturing Order: Consider two products - Product A and Product B

2.1 Assume that Product B is the raw material and has been listed in the BoM for manufacturing Product A

2.2 Assume that Product B which got consumed during production was from Lot#1 and had information filled in for the four fields (THC%, CBD%, Test Results and Lab Name) 

2.3 Upon executing the MO for Product A, Odoo prompts to assign a Lot# for the batch that just got produced. Assume we call it Lot#2 

2.4 During this entire process the Many to One field "Produced From"  on Lot#1 of Product B will be empty. However, the same field for Lot#2 of Product A after executing MO, should display Lot#1 in that field (This should be an editable field - dropdown selection as mentioned in 1.1)

2.4.1  At the same time this Lot#2 should pull the information for THC%, CBD%, Test Results, and Lab Name from Lot#1 of Product B and assign the same values to the Lot#2 of Product A
    """,
    # data files always loaded at installation
    'data': [
        'views/stock_production_lot.xml',
    ],
}
# -*- coding: utf-8 -*-
from odoo import api, fields, models

class StockProductionLot(models.Model):
    _inherit = "stock.production.lot"

    lab_name = fields.Text(string='Lab Name')
    thc_percent = fields.Float(string='THC%', digits=(3,2))
    cbd_percent = fields.Float(string='CBD%', digits=(3,2))
    
    test_results = fields.Selection(
        string='Test Results',
        selection=[('pass', 'Pass'), ('fail', 'Fail')]
    )

    produced_form = fields.Many2one(
        string='Produced Form',
        comodel_name='stock.production.lot',
        ondelete='cascade'
    )
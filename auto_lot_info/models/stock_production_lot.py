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

    @api.depends('produced_form')
    def _onchange_produced_form(self):
        for s in self:
            if s['produced_form']:
                produced_form = s['produced_form']
                s['lab_name'] = produced_form['lab_name']
                s['thc_percent'] = produced_form['thc_percent']
                s['cbd_percent'] = produced_form['cbd_percent']
                s['test_results'] = produced_form['test_results']
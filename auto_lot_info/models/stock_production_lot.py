# -*- coding: utf-8 -*-
from odoo import api, fields, models

class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

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

    sub_lots = fields.One2many(
        string='Sub Lots',
        comodel_name='stock.production.lot',
        inverse_name='produced_form',
        ondelete='cascade'
    )

    @api.constrains('lab_name', 'thc_percent', 'cbd_percent', 'test_results', 'produced_form')
    def _constrain_auto_lot_info_fields(self):
        for s in self:
            for sl in s.sub_lots:
                sl['lab_name'] = s['lab_name']
                sl['thc_percent'] = s['thc_percent']
                sl['cbd_percent'] = s['cbd_percent']
                sl['test_results'] = s['test_results']

    @api.onchange('produced_form')
    def _onchange_produced_form(self):
        for s in self:
            if s['produced_form']:
                produced_form = s['produced_form']
                s['lab_name'] = produced_form['lab_name']
                s['thc_percent'] = produced_form['thc_percent']
                s['cbd_percent'] = produced_form['cbd_percent']
                s['test_results'] = produced_form['test_results']
            else:
                s['lab_name'] = ''
                s['thc_percent'] = 0.0
                s['cbd_percent'] = 0.0
                s['test_results'] = ''

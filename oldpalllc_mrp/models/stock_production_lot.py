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

    produced_from_id = fields.Many2one(
        string='Produced From',
        comodel_name='stock.production.lot',
        ondelete='cascade'
    )

    sub_lot_ids = fields.One2many(
        string='Sub Lots',
        comodel_name='stock.production.lot',
        inverse_name='produced_from',
        ondelete='cascade'
    )

    @api.constrains('lab_name', 'thc_percent', 'cbd_percent', 'test_results')
    def _constrain_auto_lot_info_fields(self):
        for s in self:
            for sl in s.sub_lot_ids:
                sl['lab_name'] = s['lab_name']
                sl['thc_percent'] = s['thc_percent']
                sl['cbd_percent'] = s['cbd_percent']
                sl['test_results'] = s['test_results']

    def _change_produced_from(self):
        for s in self:
            if s['produced_from_id']:
                produced_from = s['produced_from_id']
                s['lab_name'] = produced_from['lab_name']
                s['thc_percent'] = produced_from['thc_percent']
                s['cbd_percent'] = produced_from['cbd_percent']
                s['test_results'] = produced_from['test_results']
            else:
                s['lab_name'] = ''
                s['thc_percent'] = 0.0
                s['cbd_percent'] = 0.0
                s['test_results'] = ''
    
    @api.constrains('produced_from_id')
    def _constrain_produced_from(self):
        self._change_produced_from()

    @api.onchange('produced_from_id')
    def _onchange_produced_from(self):
        self._change_produced_from()
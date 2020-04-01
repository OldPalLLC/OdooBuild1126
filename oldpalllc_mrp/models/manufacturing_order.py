# -*- coding: utf-8 -*-

from odoo import api, fields, models

class MrpProductProduce(models.TransientModel):
    _inherit = 'mrp.product.produce'

    def do_produce(self):
        for record in self.filtered(lambda rec: rec.finished_lot_id):
            mrp = record.production_id
            for raw_worker_order in record.raw_workorder_line_ids.filtered(lambda wl: wl.lot_id): 
                record.finished_lot_id.produced_from_id = raw_worker_order.lot_id
                record.finished_lot_id.production_id = mrp
                if mrp.mo_category != 'testing': 
                    record.finished_lot_id._change_produced_from()
        
        return super(MrpProductProduce, self).do_produce()

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    mo_category = fields.Selection(string='MO Category', selection=[('testing', 'Testing'), ('finished', 'Finished Goods')], required=True)
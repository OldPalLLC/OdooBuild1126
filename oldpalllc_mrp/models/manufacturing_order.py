# -*- coding: utf-8 -*-

from odoo import api, fields, models

class MrpProductProduce(models.TransientModel):
    _inherit = 'mrp.product.produce'

    def do_produce(self):
        for record in self.filtered(lambda rec: rec.lot_id):
            for raw_worker_order in record.raw_workorder_line_ids.filtred(lambda wl: wl.lot_id): 
                record.lot_id.produced_from = raw_worker_order.lot_id
                record.lot_id._change_produced_from()
        
        return super(MrpProductProduce, self).do_produce()
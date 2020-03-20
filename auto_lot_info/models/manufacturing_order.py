# -*- coding: utf-8 -*-
from odoo import api, fields, models

class MrpProductProduce(models.TransientModel):
    _inherit = 'mrp.product.produce'

    def do_produce(self):
        for s in self:
            lot1 = s.finished_lot_id
            for m in s.raw_workorder_line_ids:
                if lot1: 
                    lot2 = m.lot_id
                    if lot2:
                        lot1[0].produced_from = lot2[0]
        
        return super(MrpProductProduce, self).do_produce()
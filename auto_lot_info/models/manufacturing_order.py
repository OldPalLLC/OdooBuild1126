# -*- coding: utf-8 -*-
from odoo import api, fields, models

class MrpProductProduce(models.TransientModel):
    _inherit = 'mrp.product.produce'

    def do_produce(self):
        result = super(MrpProductProduce, self).do_produce()

        print()
        for s in self:
            lot1 = s.finished_lot_id
            print(lot1)
            for m in s.raw_workorder_line_ids:
                if lot1: 
                    lot2 = m.lot_id
                    print(lot2)
                    if lot2:
                        lot1[0].produced_from = lot2[0]

        return result
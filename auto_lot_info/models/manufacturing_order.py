# -*- coding: utf-8 -*-
from odoo import api, fields, models

class MrpProductProduce(models.TransientModel):
    _inherit = 'mrp.product.produce'

    def do_produce(self):
        result = super(MrpProductProduce, self).do_produce()

        for s in self:
            lot2 = s.finished_lot_id
            for m in s.raw_workorder_line_ids:
                if lot2: 
                    lot1 = m.lot_id
                    if lot1:
                        lot1[0].produced_from = lot2[0]

        return result
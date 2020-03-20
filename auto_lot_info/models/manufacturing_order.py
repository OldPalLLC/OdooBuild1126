# -*- coding: utf-8 -*-
from odoo import api, fields, models

class ManufacturingOrder(models.Model):
    _inherit = 'mrp.production'

    def action_assign(self):
        result = super(ManufacturingOrder, self).action_assign()
        Lot = self.env['stock.production.lot']
        for s in self:
            for m in s.move_raw_ids:
                lot2 = Lot.search([('product_id', '=', m.product_id.id)])
                if lot2: 
                    lot1 = Lot.search([('product_id', '=', s.product_id.id)])
                    if lot1:
                        lot1[0].produced_form = lot2[0]
        return result
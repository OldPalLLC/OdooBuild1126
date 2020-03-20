# -*- coding: utf-8 -*-
import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class MrpProductProduce(models.TransientModel):
    _inherit = 'mrp.product.produce'

    def do_produce(self):
        for s in self:
            lot1 = s['finished_lot_id']
            for m in s['raw_workorder_line_ids']:
                if lot1: 
                    _logger.info("lot1: {}".format(lot1['name']))
                    lot2 = m['lot_id']
                    if lot2:
                        _logger.info("lot2: {}".format(lot2['name']))
                        lot1[0]['produced_from'] = lot2[0]
        
        return super(MrpProductProduce, self).do_produce()
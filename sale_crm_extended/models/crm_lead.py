# -*- coding: utf-8 -*-

from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    def action_view_sale_quotation(self):
        action = self.env.ref('sale_crm_extended.action_crm_quotations').read()[0]
        print("called")
        action['context'] = {
            'search_default_draft': 1,
            'search_default_partner_id': self.partner_id.id,
            'default_partner_id': self.partner_id.id,
            'default_opportunity_id': self.id,
            'hide_confirm': True
        }
        action['domain'] = [('opportunity_id', '=', self.id), ('state', 'in', ['draft', 'sent'])]
        quotations = self.mapped('order_ids').filtered(lambda l: l.state in ('draft', 'sent'))
        if len(quotations) == 1:
            action['views'] = [(self.env.ref('sale.view_order_form').id, 'form')]
            action['res_id'] = quotations.id
        return action

    def action_new_quotation(self):
        action = super(CrmLead, self).action_new_quotation()
        action['context'].update({'hide_confirm': True})
        return action

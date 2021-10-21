from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    construction_site_count = fields.Integer(compute='_get_site_count')

    def action_construction_site(self):
        construction_site_count = self.env["construction.site"].search_count(
            [("general_contractor_purchase_order_id", "=", self.id)])
        construction_site = False

        if construction_site_count == 1:
            construction_site = self.env["construction.site"].search(
                [("general_contractor_purchase_order_id", "=", self.id)]).id
            view_mode = "form"
        
        else: 
            view_mode = "tree,form"
        
        return {
            "type": "ir.actions.act_window",
            "view_mode":view_mode,
            "name": "construction site",
            "res_model": "construction.site",
            "domain": [("general_contractor_purchase_order_id", "=", self.id)],
            "target": "current",
            "res_id": construction_site
        }

    def _get_site_count(self):
        for rec in self:
            rec.construction_site_count = self.env["construction.site"].search_count(
                [("general_contractor_purchase_order_id", "=", self.id)])


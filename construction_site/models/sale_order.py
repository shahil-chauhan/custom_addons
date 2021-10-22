from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    construction_site_count = fields.Integer(compute="_get_site_count")

    def action_construction_site(self):
        construction_site = False
        construction_site_count = self.env["construction.site"].search_count(
            [("sale_order_id", "=", self.id)]
        )

        if construction_site_count == 1:
            construction_site = (
                self.env["construction.site"]
                .search([("sale_order_id", "=", self.id)])
                .id
            )
            view_mode = "form"

        else:
            view_mode = "tree,form"

        return {
            "type": "ir.actions.act_window",
            "view_mode": view_mode,
            "name": "construction site",
            "res_model": "construction.site",
            "domain": [("sale_order_id", "=", self.id)],
            "target": "current",
            "res_id": construction_site,
        }

    def _get_site_count(self):
        for rec in self:
            rec.construction_site_count = self.env["construction.site"].search_count(
                [("sale_order_id", "=", self.id)]
            )

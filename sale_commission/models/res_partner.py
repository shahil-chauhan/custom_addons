# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.tools.translate import _


class ResPartner(models.Model):
    _inherit = "res.partner"

    sale_order_line_total = fields.Float(
        string="Sale Commission History", compute="_compute_sale_order_line_total"
    )

    # To compute the total of order line
    def _compute_sale_order_line_total(self):
        lines = (
            self.env["sale.order"]
            .search([("partner_id", "=", self.id)])
            .mapped("order_line")
        )
        self.sale_order_line_total = sum([line.price_subtotal for line in lines])

    # action to open the action for sale order line
    def action_view_sale_order_line(self):
        lines = (
            self.env["sale.order"]
            .search([("partner_id", "=", self.id)])
            .mapped("order_line")
        )
        return {
            "type": "ir.actions.act_window",
            "view_mode": "tree",
            "name": "Sale Order Lines",
            "res_model": "sale.order.line",
            "domain": [("id", "in", lines.ids)],
            "target": "new",
        }

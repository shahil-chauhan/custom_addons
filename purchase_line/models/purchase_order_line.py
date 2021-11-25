# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    order_line_cus = fields.Char(string="Order Line")

    # this method is used to transfer data from "purchase.order.line" to "account.move.line"
    def _prepare_account_move_line(self):
        res = super(PurchaseOrderLine, self)._prepare_account_move_line()
        res.update(
            {
                "order_line_cus": self.order_line_cus,
            }
        )
        return res


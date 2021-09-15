# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "sale.order"

    @api.model
    def demo_cron(self):
        print("\n\n\n\ncron called------")
        orders_pending = self.env["sale.order"].search(
            [("state", "not in", ("sale", "done"))]
        )
        print("\n\n\n\nOrders Pending------", orders_pending)

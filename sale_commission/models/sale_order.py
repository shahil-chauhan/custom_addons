# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.tools.translate import _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    commission = fields.Float(string=_("Commission (%)"), default=2.5)


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    production_commission = fields.Float(
        string=_("Production Commission"), compute="_compute_commission"
    )

    @api.depends("price_subtotal", "order_id.commission")
    def _compute_commission(self):
        for record in self:
            record.production_commission = record.price_subtotal * (
                record.order_id.commission / 100
            )

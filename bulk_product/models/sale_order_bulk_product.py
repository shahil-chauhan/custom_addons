# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.tools.translate import _


class SaleOrderBulkProduct(models.Model):
    _inherit = "sale.order"

    bulk_product_template_id = fields.Many2one(
        "bulk.products", string=_("Bulk Products")
    )

    @api.onchange("bulk_product_template_id")
    def order_line_add(self):
        for pr_id in self.bulk_product_template_id.bulk_products_ids.ids:
            self.write({"order_line": [(0, 0, {"product_id": pr_id})]})

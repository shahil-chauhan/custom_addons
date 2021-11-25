from odoo import api, fields, models
from odoo.tools.translate import _


class SaleOrderBulkProducts(models.Model):
    _inherit = "sale.order"

    bulk_product_template_id = fields.Many2one(
        "bulk.products", string=_("Bulk Products")
    )

    @api.onchange("bulk_product_template_id")
    def order_line_add(self):
        order_lines = [(5, 0, 0)]
        for bulk_product in self.bulk_product_template_id.bulk_products_ids:
            data = {
                "product_id": bulk_product.product_id.id,
                "name": bulk_product.product_id.name,
                "price_unit": bulk_product.product_id.lst_price,
                'product_uom': bulk_product.product_id.uom_id.id,
            }
            order_lines.append((0, 0, data))
        self.order_line = order_lines

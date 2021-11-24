from odoo import api, fields, models
from odoo.tools.translate import _


class SaleOrderBulkProducts(models.Model):
    _inherit = "sale.order"

    bulk_product_template_id = fields.Many2one(
        "bulk.products", string=_("Bulk Products")
    )

    @api.onchange('bulk_product_template_id')
    def order_line_add(self):
        self.write({'order_line': [(5, 0, 0)]})
        for pro in self.bulk_product_template_id.bulk_products_ids:
            self.sudo().write({'order_line': [(0, 0, {'product_id': pro.product_id, 'name': pro.name})]})

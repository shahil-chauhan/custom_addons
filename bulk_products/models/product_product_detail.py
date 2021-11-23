from odoo import api, fields, models
from odoo.tools.translate import _


class BulkProducts(models.Model):
    _inherit = "product.product"
    _description = " many2one of product.product"

    bulk_product_id = fields.Many2one("bulk.products", string=_("Bulk Products"))
    product_product_id = fields.Many2one("product.product", domain="[('type', '=', 'product')]",
                                         string=_("Bulk Products"))

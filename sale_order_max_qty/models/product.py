from odoo import api, fields, models
from odoo.tools.translate import _


class ProductProduct(models.Model):
    _inherit = "product.product"

    qty_on_order = fields.Float(string=_("Qty On Order"), default=1.0)

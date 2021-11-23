# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.tools.translate import _


class BulkProducts(models.Model):
    _name = "bulk.products"
    _description = "module for bulk product"

    name = fields.Char(string=_("Name"))
    master_product = fields.Many2one("product.template", string=_("Master Product"))
    bulk_products_ids = fields.One2many(
        "product.product", "bulk_product_id", string=_("Bulk Products")
    )
    user = fields.Many2one("res.partner", string=_("User"))
    email = fields.Char(string=_("Email"))

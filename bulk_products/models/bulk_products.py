# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.tools.translate import _


class BulkProducts(models.Model):
    _name = "bulk.products"
    _description = "model for bulk product"

    name = fields.Char(string=_("Name"))
    master_product_id = fields.Many2one("product.template", string=_("Master Product"))
    bulk_products_ids = fields.One2many(
        "bulk.product.line", "bulk_product_id", string=_("Bulk Products")
    )
    user_id = fields.Many2one("res.partner", string=_("User"))
    email = fields.Char(string=_("Email"))


class BulkProductsLine(models.Model):
    _name = "bulk.product.line"
    _description = "model for bulk product line"

    name = fields.Char(related='product_id.name')
    product_id = fields.Many2one("product.product", domain="[('type', '=', 'product')]", string=_("Products"))
    bulk_product_id = fields.Many2one("bulk.products")

# -*- coding: utf-8 -*-
from odoo import fields, models
from odoo.tools.translate import _


class BulkProducts(models.Model):
    _name = "product.product.fields"
    _description = "product.product many2one"

    product_product_id = fields.Many2one(
        "product.product", domain="[('type', '=', 'product')]", string=_("Product")
    )
    bulk_product_id = fields.Many2one("bulk.products", string="Bulk Products")

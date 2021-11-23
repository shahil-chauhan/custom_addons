# -*- coding: utf-8 -*-
from odoo import fields, models
from odoo.tools.translate import _


class BulkProducts(models.Model):
    _name = "bulk.products"
    _description = "Bulk Products"

    name = fields.Char(string=_("Name"), required=True)
    master_product_id = fields.Many2one("product.template", string=_("Master Product"))
    bulk_products_ids = fields.One2many(
        "product.product.fields", "bulk_product_id", string=_("Bulk Products")
    )
    res_partner_id = fields.Many2one("res.partner", string=_("User"))
    email = fields.Char(string=_("Email"))

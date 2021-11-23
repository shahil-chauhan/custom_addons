from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    or_name = fields.Char(string="Product name", default="KBC")

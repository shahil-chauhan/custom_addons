from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    order_line_cus = fields.Char(string="Order Line")

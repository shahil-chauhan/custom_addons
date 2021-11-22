from odoo import fields, models
from odoo.tools.translate import _


class OrderTracking(models.Model):
    _name = "order.track"
    _description = "Tracking order"

    sales_order_ref = fields.Many2one("sale.order", string=_("Sales Order Ref"))
    user_name = fields.Many2one("res.users", string=_("UserName"))

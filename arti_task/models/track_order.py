from odoo import fields, models
from odoo.exceptions import UserError


class OrderTracking(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        for record in self:
            print("\n\n\nhello\n\n\n")
            if len(record.order_line) == 0:
                print("\n\n\no na na na..\n\n\n")
                raise UserError("you are not eligible to get this rank!!!!!......")

        return super(OrderTracking, self).action_confirm()

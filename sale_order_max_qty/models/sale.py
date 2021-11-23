from odoo import api, fields, models
from odoo.tools.translate import _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    total_capacity = fields.Float(string=_("Total Capacity"), readonly=True)

    def total_cap_on_button_click(self):

        for order in self:
            total_capacity = 0
            for line in order.order_line:
                total_capacity += line.max_qty_allowed
            order.update({"total_capacity": total_capacity})


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    # max_qty_allowed = fields.Float(related="product_id.qty_on_order", string=_("Max Qty Allowed"))
    # max_qty_allowed = fields.Float(string=_("Max Qty Allowed"))
    max_qty_allowed = fields.Float(
        string=_("Max Qty Allowed"), compute="_compute_onchange_max_qty_allowed"
    )

    @api.onchange("product_id")
    def onchange_max_qty_allowed(self):
        for r in self:
            r.max_qty_allowed = r.product_id.qty_on_order

    @api.depends("product_id")
    def _compute_onchange_max_qty_allowed(self):
        for r in self:
            r.max_qty_allowed = r.product_id.qty_on_order


# product_id = fields.Many2one(
#         'product.product', string='Product', domain="[('sale_ok', '=', True), '|', ('company_id', '=', False), ('company_id', '=', company_id)]",
#         change_default=True, ondelete='restrict', check_company=True

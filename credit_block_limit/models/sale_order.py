from odoo import api, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def create(self, values):
        sale_order = super(SaleOrder, self).create(values)
        credit_limit = sale_order.partner_id.credit_limit
        blocking_limit = sale_order.partner_id.blocking_limit
        credit_limit_score = sale_order.partner_id.credit_limit_score
        blocking_limit_score = sale_order.partner_id.blocking_limit_score
        amount_total = sale_order.amount_total

        email_to = (self.env["ir.config_parameter"].sudo().get_param("credit_block_limit.notify_person"))
        # to check for the credit limit
        if credit_limit_score and credit_limit:
            for order in self.env["sale.order"].search(
                    [("partner_id", "=", sale_order.partner_id.id), ("state", "=", "draft")]):
                amount_total += order.amount_total
            if amount_total > credit_limit_score:
                if email_to:
                    template = sale_order.env.ref(
                        "credit_block_limit.limit_mail_template"
                    )
                    template.send_mail(sale_order.id, email_values={"email_to": email_to}, force_send=True)

                    super(SaleOrder, self).unlink()  # to unlink the record
                    self._cr.commit()
                raise ValidationError(
                    _('“Your Sale Order Credit Limit has been Exceeded."')
                )

        # to check for the blocking limit
        if blocking_limit_score and blocking_limit:
            for order in self.env["sale.order"].search(
                    [("partner_id", "=", sale_order.partner_id.id), ("state", "=", "sale")]
            ):
                amount_total += order.amount_total
            if amount_total > blocking_limit_score:
                if email_to:
                    template = sale_order.env.ref(
                        "credit_block_limit.limit_mail_template"
                    )
                    template.send_mail(
                        sale_order.id, email_values={"email_to": email_to}
                    )
                    salesuper(SaleOrder, self).unlink()  # to unlink the record
                    self._cr.commit()

                raise ValidationError(
                    _("“You cannot create SO as the Block Limit has been Exceeded”")
                )
        return sale_order

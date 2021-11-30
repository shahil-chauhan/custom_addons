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
        email_to = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("credit_block_limit.notify_person")
        )
        print("\n\nemail", email_to)

        # to check for the credit limit
        if credit_limit_score and credit_limit:
            total = sale_order.amount_total
            for order in self.env["sale.order"].search(
                [("partner_id", "=", sale_order.partner_id.id), ("state", "=", "draft")]
            ):
                total += order.amount_total
            if total > credit_limit_score:
                if email_to:
                    template = sale_order.env.ref(
                        "credit_block_limit.limit_mail_template"
                    )
                    print("\n\nemailtemplate ", template)

                    temp = template.send_mail(sale_order.id, force_send=True)
                    print("\n\nemail sent ", temp)
                raise ValidationError(
                    _('“Your Sale Order Credit Limit has been Exceeded."')
                )

        # to check for the blocking limit
        if blocking_limit_score and blocking_limit:
            amount_total = sale_order.amount_total
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
                raise ValidationError(
                    _("“You cannot create SO as the Block Limit has been Exceeded”")
                )
        return sale_order

from datetime import datetime

from odoo import _, http
from odoo.http import request


class PaymentPortal(http.Controller):
    """this url for form page open"""

    @http.route(
        "/my/bulk_product",
        type="http",
        auth="user",
        website=True,
    )
    def bulk_product_menu_show(self):
        product_template_data = request.env["product.template"].search([])
        vals = {"product_template_data": product_template_data}
        return request.render("bulk_product.bulk_product_form", vals)

    """this url for successfully created bulk order"""

    @http.route("/my/bulk_product/submit", type="http", auth="user", website=True)
    def portal_submit_success(self, **post):
        if post:
            partner_create = {
                "name": post.get("partner_name"),
                "phone": post.get("phone"),
                "email": post.get("email"),
            }
            request.env["res.partner"].sudo().create(partner_create)
            bulk_record_create = {
                "name": post.get("name"),
                "master_product_id": int(post.get("master_product_name")),
                "res_partner_id": request.env["res.partner"].search([]).ids[-1],
                "email": post.get("email"),
            }
            request.env["bulk.products"].sudo().create(bulk_record_create)

        return request.render("bulk_product.bulk_product_form_success")

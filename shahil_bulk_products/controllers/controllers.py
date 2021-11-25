# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, route


class BulkProduct(http.Controller):
    """URL for the form opening"""

    @http.route("/bulk_product", type="http", website=True, auth="public", csrf=False)
    def bulk_product_home(self, **kw):
        master_product = request.env["product.template"].sudo().search([])
        return request.render(
            "shahil_bulk_products.bulk_product_template", {"master_product": master_product}
        )

    """ URL for the form submission"""

    @http.route(
        "/bulk_product/submit", type="http", website=True, auth="public", csrf=False
    )
    def bulk_product(self, **kw):
        if kw:
            create_partner = {
                "name": kw.get("partner_name"),
                "email": kw.get("email"),
                "phone": kw.get("phone"),
            }
            new_partner = request.env["res.partner"].sudo().create(create_partner)

            bulk_product_record = {
                "name": kw.get("name"),
                "master_product_id": kw.get("master_product_id"),
                "user_id": new_partner.id,
                # "user_id": request.env["res.partner"].search([]).ids[-1],
                "email": kw.get("email"),
            }
            request.env["bulk.products"].sudo().create(bulk_product_record)

        return request.render("shahil_bulk_products.form_submitted")

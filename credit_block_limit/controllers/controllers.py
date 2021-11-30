# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request, route


class Controller(http.Controller):
    @http.route("/partner_info", type="http", website=True, auth="public", csrf=False)
    def partner(self, **kw):
        partners = request.env["res.partner"].sudo().search([])
        return request.render(
            "credit_block_limit.partner_info_template", {"partners": partners}
        )

    @http.route(
        "/partner_details", type="http", website=True, auth="public", csrf=False
    )
    def contact_details(self, partners):
        states = request.env["res.country.state"].sudo().search([])
        countries = request.env["res.country"].sudo().search([])
        if partners:
            partner_id = int(partners)
            partner = (
                request.env["res.partner"].sudo().search([("id", "=", partner_id)])
            )
        return request.render(
            "credit_block_limit.partner_form_template",
            {"partner": partner, "countries": countries, "states": states},
        )

    # TO UPDATE THE DATA IN BACKEND
    @http.route("/partner_update", type="http", website=True, auth="public", csrf=False)
    def partner_update(self, **kw):
        print("\n\n\n\nkw-----------------", kw)
        partner_id = kw.get("partner_id", False)
        del kw["partner_id"]
        partner_obj = request.env["res.partner"].sudo()
        partner = False
        if "state_id" in kw and kw.get("state_id"):
            kw["state_id"] = int(kw["state_id"])
        else:
            kw["state_id"] = False
        if "country_id" in kw and kw.get("country_id"):
            kw["country_id"] = int(kw["country_id"])
        else:
            kw["country_id"] = False

        if partner_id:
            partner = partner_obj.browse(int(partner_id))
            partner.write(kw)
        else:
            partner = partner_obj.create(kw)
        return request.render("credit_block_limit.partner_updated_template")

# -*- coding: utf-8 -*-
import json

from odoo import http
from odoo.http import request, route


class Contact(http.Controller):
    @http.route("/contact", type="http", website=True, auth="public", csrf=False)
    def demo_page(self, **kw):
        contacts = request.env["res.partner"].sudo().search([])
        return request.render("contact_session.contacts_list", {"contacts": contacts})

    @http.route(
        "/contact/<model('res.partner'):contact>",
        type="http",
        website=True,
        auth="public",
    )
    def contact_details(self, contact):
        states = request.env["res.country.state"].sudo().search([])
        countries = request.env["res.country"].sudo().search([])
        return request.render(
            "contact_session.contact_form_template",
            {
                "partner": contact,
                "countries": countries,
                "states": states,
            },
        )

    @http.route("/contact_form", type="http", website=True, auth="public", csrf=True)
    def create_new_contact(self):
        states = request.env["res.country.state"].sudo().search([])
        countries = request.env["res.country"].sudo().search([])
        return request.render(
            "contact_session.contact_form_template",
            {
                "countries": countries,
                "states": states,
            },
        )

    @http.route("/contact_update", type="http", website=True, auth="public", csrf=False)
    def contact_update(self, **kw):
        partner_id = kw.get("partner_id", False)
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

        if "team_lead" not in kw:
            kw["team_lead"] = False

        if partner_id:
            partner = partner_obj.browse(int(partner_id))
            del kw["partner_id"]
            partner.write(kw)
        else:
            partner = partner_obj.create(kw)
        return request.redirect("/contact/%s" % partner.id)

# -*- coding: utf-8 -*-
import json

from odoo import http
from odoo.http import request, route
import base64


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
        domain = []
        if contact.country_id:
            domain.append(('country_id', '=', contact.country_id.id))
        states = request.env["res.country.state"].sudo().search(domain)
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
    def create_new_contact(self, **kw):
        states = request.env["res.country.state"].sudo().search([])
        countries = request.env["res.country"].sudo().search([])
        return request.render(
            "contact_session.contact_form_template",
            {
                "countries": countries,
                "states": states,
            },
        )

    @http.route("/get/filtered/states", type="json", auth="public")
    def get_filtered_states(self, **kw):
        data = {'status': False, 'error': False, 'states': False}
        try:
            domain = []
            if 'country_id' in kw and kw.get('country_id', False):
                domain.append(('country_id', '=', int(kw.get('country_id'))))
            states = request.env["res.country.state"].sudo().search_read(domain, ['id', 'name'])
            data['states'] = states
            data['status'] = True
        except Exception as e:
            data['error'] = e
        return data


    @http.route("/get/error/dialog", type="json", auth="public")
    def get_error_dialog(self, **kw):
        markup = request.env['ir.ui.view'].sudo()._render_template('contact_session.error_dialog_template', kw)
        return markup

    @http.route("/contact_update", type="http", website=True, auth="public", csrf=False)
    def contact_update(self, **kw):
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

        if "team_lead" not in kw:
            kw["team_lead"] = False

        if "delete_image" in kw and kw.get("delete_image") == "True":
            kw["image_1920"] = False
        else:
            if "image_1920" in kw and kw.get("image_1920"):
                kw["image_1920"] = base64.b64encode(kw["image_1920"].read())
        del kw["delete_image"]

        if partner_id:
            partner = partner_obj.browse(int(partner_id))
            partner.write(kw)
        else:
            partner = partner_obj.create(kw)
        return request.redirect("/contact/%s" % partner.id)

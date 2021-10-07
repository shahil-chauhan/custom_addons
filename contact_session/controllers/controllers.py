# -*- coding: utf-8 -*-
import json

from odoo import http
from odoo.http import request, route


class Contact(http.Controller):
    @http.route("/contact", type="http", website=True, auth="public")
    def demo_page(self):
        contact = request.env["res.partner"].sudo().search([])
        return request.render("contact_session.contacts_list", {"contacts": contact})

    @http.route("/contact/<model('res.partner'):contact>", type="http", website=True, auth="public")
    def contact_details(
            self, contact, **kw):
        contacts = request.env["res.partner"].sudo().browse([])

        return request.render("contact_session.contact_detail", {"contact_detail": contact, "contact": contacts})

    # @http.route("/partner_update", type="http", website=True, auth="public", csrf=False)
    # def partner_update(self, **kw):
    #     partner = request.env["res.partner"].sudo().browse(int(kw.get('id')))
    #     partner.write({
    #         'name': kw.get('name')
    #     })
    #     return request.redirect("/contact/%s" % partner.id)
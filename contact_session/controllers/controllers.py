# -*- coding: utf-8 -*-
import json

from odoo import http
from odoo.http import request, route


class Contact(http.Controller):
    @http.route("/contact", type="http", website=True, auth="public")
    def demo_page(self):
        contact = request.env["res.partner"].sudo().search([])
        return request.render("contact_session.contacts_list", {"contacts": contact})


class ContactDetails(http.Controller):
    @http.route("/contact/<model('res.partner'):contact>", type="http", website=True, auth="public")
    def contact_details(self, contact, **kw):
        return request.render("contact_session.contact_detail", {"contact_detail": contact})

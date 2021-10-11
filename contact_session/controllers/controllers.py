# -*- coding: utf-8 -*-
import json

from odoo import http
from odoo.http import request, route


class Contact(http.Controller):
    @http.route("/contact", type="http", website=True, auth="public")
    def demo_page(self):
        # contact = request.env["res.partner"].sudo().search([], order="name asc")
        contacts = request.env["res.partner"].sudo().search([])
        return request.render("contact_session.contacts_list", {"contacts": contacts})

    @http.route("/contact/<model('res.partner'):contact>", type="http", website=True, auth="public")
    def contact_details(self, contact, **kw):
        return request.render("contact_session.contact_details", {"contact_details": contact})

    @http.route("/contact_form", type="http", website=True, auth="public", csrf=True)
    def create_new_contact(self):
        return request.render("contact_session.contact_form_template")









    # @http.route("/partner_update", type="http", website=True, auth="public", csrf=False)
    # def partner_update(self, **kw):
    #     partner = request.env["res.partner"].sudo().browse(int(kw.get('id')))
    #     partner.write({
    #         'name': kw.get('name')
    #     })
    #     return request.redirect("/contact/%s" % partner.id)

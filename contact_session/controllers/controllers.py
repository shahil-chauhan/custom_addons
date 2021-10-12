# -*- coding: utf-8 -*-
import json

from odoo import http
from odoo.http import request, route


class Contact(http.Controller):
    @http.route("/contact", type="http", website=True, auth="public", csrf=False)
    def demo_page(self, **kw):
        contacts = request.env["res.partner"].sudo().search([])
        print("\n\n\n\n\n\n\n kw =========>>", kw)
        if kw:
            vals = {
                'name': kw.get('name'),
                'email': kw.get('email'),
                'phone': kw.get('phone'),
            }
            print("=============vals==============", vals)
            
            request.env["res.partner"].sudo().create(vals)
            return request.redirect("/contact")
        else:
            return request.render("contact_session.contacts_list", {"contacts": contacts})

    # _sql_constraints = [('email_unique', 'UNIQUE(email)', 'The email must be unique')]

    @http.route("/contact/<model('res.partner'):contact>", type="http", website=True, auth="public")
    def contact_details(self, contact, **kw):
        return request.render("contact_session.contact_details", {"contact_details": contact})

    @http.route("/contact_form", type="http", website=True, auth="public", csrf=True)
    def create_new_contact(self):

        return request.render("contact_session.contact_form_template")

    @http.route("/contact_update", type="http", website=True, auth="public", csrf=False)
    def contact_update(self, **kw):
        contact = request.env["res.partner"].sudo().browse(int(kw.get('id')))
        contact.write({
            'name': kw.get('name'),
            'email': kw.get('email'),
            'phone': kw.get('phone'),
        })
        return request.redirect("/contact")

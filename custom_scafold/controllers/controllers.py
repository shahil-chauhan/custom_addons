# -*- coding: utf-8 -*-
# from odoo import http
# from odoo.http import request, route

# class BulkProduct(http.Controller):
#     @http.route('/bulk_product/', type="http", website=True, auth="public", csrf=False)
#     def bulk_product(self, **kw):
#         master_product = request.env['product.template'].sudo().search([])
#         return request.render("bulk_products.bulk_product_template", {'master_product': master_product})
#
#     @http.route('/bulk_product/submit', type="http", website=True, auth="public", csrf=False)
#     def bulk_product(self, **kw):
#         if kw:
#             create_partner = {
#                 'name': kw.get("partner_name"),
#             }
#             request.env["create.employees"].sudo().create(create_partner)
#         return request.render("bulk_products.")

# -*- coding: utf-8 -*-
# from odoo import http


# class CustomScafold(http.Controller):
#     @http.route('/custom_scafold/custom_scafold/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_scafold/custom_scafold/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_scafold.listing', {
#             'root': '/custom_scafold/custom_scafold',
#             'objects': http.request.env['custom_scafold.custom_scafold'].search([]),
#         })

#     @http.route('/custom_scafold/custom_scafold/objects/<model("custom_scafold.custom_scafold"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_scafold.object', {
#             'object': obj
#         })

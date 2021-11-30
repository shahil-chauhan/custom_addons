# # -*- coding: utf-8 -*-
#
# from odoo import models, fields, api
# from odoo.tools.translate import _
#
#
# class custom_scafold(models.Model):
#     _name = ''
#     _description = 'Model for '
#
#     name = fields.Char()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

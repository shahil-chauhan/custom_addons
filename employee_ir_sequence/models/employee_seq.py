# -*- coding: utf-8 -*-

from odoo import api, fields, models


class EmployeeSequence(models.Model):
    _inherit = "hr.employee"

    sequence = fields.Char()

    @api.model
    def create(self, vals):
        vals["sequence"] = (
            self.env["ir.sequence"].next_by_code("sequence.code") or "New"
        )
        print("\n\n\n\nvals: ", vals["sequence"])
        return super(EmployeeSequence, self).create(vals)

    def name_wizard(self):
        pass

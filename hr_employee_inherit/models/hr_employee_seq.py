# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class HrEmployeeInherit(models.Model):
    _inherit = "hr.employee"

    sequence = fields.Char(
        string="Hr Employee Sequence",
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _("New"),
    )

    @api.model
    def create(self, vals):
        if vals.get("sequence", _("New")) == _("New"):
            vals["sequence"] = self.env["ir.sequence"].next_by_code(
                "hr.employee.seq"
            ) or _("New")
            return super(HrEmployeeInherit, self).create(vals)

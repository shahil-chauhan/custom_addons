# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class HrEmployeeWizard(models.TransientModel):
    _name = "hr.employee.wizard"
    _description = "Hr employee module to add a wizard"

    phone = fields.Char()

    @api.onchange("name")
    def hr_employee_wizard(self):
        context = self._context
        emp = self.env["hr.employee"].browse(context["active_id"])
        emp.mobile_phone = self.phone

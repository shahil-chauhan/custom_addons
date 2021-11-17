from odoo import fields, models
from odoo.tools.translate import _


class HrJob(models.Model):
    _inherit = "hr.job"

    affordable_salary = fields.Integer(string=_("Affordable Salary"))

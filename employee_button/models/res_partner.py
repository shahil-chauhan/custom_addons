from odoo import _, api, fields, models
from odoo.osv import expression


class ResPartner(models.Model):
    _inherit = "res.partner"

    no_con = fields.Char()

    def open_view_employee_list(self):
        print("open_view_employee_list")
        return {
            "name": self.name,
            "type": "ir.actions.act_window",
            "view_type": "kanban",
            "view_mode": "kanban",
            "view_id": self.env.ref("hr.hr_kanban_view_employees").id,
            "res_model": "hr.employee",
        }

    def concatenate_mobile_ph_no(self):
        print("\n\n\n\n\n concatenate_mobile_ph_no callinggggg..")
        concate = str(self.phone) + str(self.mobile)
        self.no_con = concate

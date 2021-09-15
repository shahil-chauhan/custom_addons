from odoo import fields, models


class HrApplication(models.Model):
    _name = "hr.referral.application"
    _description = "reference model"

    name = fields.Char(string="Name", copy=False)
    email = fields.Char(string="Email", copy=False)
    referral_id = fields.Many2one("hr.employee", string="Referral Name")
    degree_id = fields.Many2one("hr.recruitment.degree", string="Degree")
    department_id = fields.Many2one("hr.job", string="Department")
    expected_salary = fields.Float(string="Expected Salary")
    summary = fields.Text(string="Summary")
    expected_doj = fields.Date(string="Expected Joining Date")
    state = fields.Selection(
        [("draft", "Draft"), ("approved", "Approved"), ("cancel", "Cancel")],
        default="draft",
    )
    currency_id = fields.Many2one("res.currency", string="Currency")

    def action_approvel(self):
        for rec in self:
            rec.write({"state": "approved"})

    def action_cancel(self):
        for rec in self:
            rec.state = "cancel"

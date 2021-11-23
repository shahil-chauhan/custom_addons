from datetime import date

from dateutil import relativedelta

from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _


class CreateEmployees(models.Model):
    _name = "create.employees"
    _description = "Create Employees"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string=_("Name"), required=True, tracking=True)
    birth_date = fields.Date(string=_("Birth Date"), required=True, tracking=True)
    age = fields.Integer(string=_("Age"), tracking=True)
    street = fields.Char(string=_("Street"), tracking=True)
    state = fields.Many2one("res.country.state", string=_("State"))
    country = fields.Many2one("res.country", string=_("Country"))
    city = fields.Char(string=_("City"), tracking=True)
    email = fields.Char(string=_("Email"), required=True, tracking=True)
    phone = fields.Char(string=_("Phone"), required=True, tracking=True)
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("other", "Other")]
    )
    experience_info = fields.Text(string=_("Experience Info"))
    expected_salary = fields.Integer(string=_("Expected Salary"))
    job_position = fields.Many2one("hr.job", string=_("Job Position"))
    affordable_salary = fields.Integer(
        related="job_position.affordable_salary", string=_("Affordable Salary")
    )
    extra_amount = fields.Float(string=_("Extra Amount"))
    yearly_amount = fields.Float(string=_("Yearly Amount"))
    monthly_amount = fields.Float(string=_("Monthly Amount"))
    start_date = fields.Date(string=_("Start Date"))
    end_date = fields.Date(string=_("End Date"))
    button_hide = fields.Char(compute="_button_hide", invisible=True)

    def compute_age(self):
        for rec in self:
            if rec.birth_date:
                rec.age = relativedelta.relativedelta(
                    date.today(), rec.birth_date
                ).years
            if rec.age < 18:
                raise UserError(_("The Employee age cannot be less than 18 years."))

    # @api.depends("start_date", "end_date")
    # def compute_amount(self):
    #     for rec in self:
    #         diff = relativedelta.relativedelta(rec.start_date, rec.end_date)
    #         if diff.year == 0 and diff.months >= 1:
    #             rec.monthly_amount = rec.expected_salary + \
    #                 rec.extra_amount + rec.affordable_salary
    #         elif diff.year >= 1:
    #             rec.yearly_amount = rec.expected_salary + rec.extra_amount

    def calculate_yearly(self):
        self.yearly_amount = self.expected_salary + self.extra_amount

    def calculate_monthly(self):
        self.monthly_amount = (
            self.expected_salary + self.extra_amount + self.extra_amount
        )

    @api.depends("start_date", "end_date")
    def _button_hide(self):
        if self.start_date and self.end_date:
            diff = relativedelta.relativedelta(self.end_date, self.start_date)
            if diff.years:
                self.button_hide = "year"
            elif diff.months:
                self.button_hide = "month"
            else:
                self.button_hide = False
        else:
            self.button_hide = False

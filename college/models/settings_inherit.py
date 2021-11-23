import calendar
from ast import literal_eval
from datetime import date, datetime

from odoo import _, api, fields, models


class Settings(models.TransientModel):
    _inherit = "res.config.settings"

    def _get_domain(self):
        _, num_days = calendar.monthrange(datetime.now().year, datetime.now().month)
        first_day, last_day = (
            datetime.today().replace(day=1),
            datetime.today().replace(day=num_days),
        )
        partners = (
            self.env["sale.order"]
            .search([("date_order", ">=", first_day), ("date_order", "<=", last_day)])
            .mapped("partner_id")
        )
        return [("id", "in", partners.ids)]

    active = fields.Boolean(string=_("active"))
    url = fields.Char(
        string=_("URL"),
        config_parameter="college.param.url",
        default="https://www.google.com/",
    )
    module_google_calendar = fields.Boolean(string=_("Google Calendar"))
    partner_ids = fields.Many2many(
        "res.partner",
        "res_partner_rel",
        "partner_id",
        string=_("Customers"),
        domain=_get_domain,
    )

    @api.model
    def get_values(self):
        res = super(Settings, self).get_values()
        active = self.env["ir.config_parameter"].get_param("college.active")
        partner_ids = self.env["ir.config_parameter"].get_param("college.partner_ids")
        res.update(
            active=active,
        )
        if partner_ids:
            res.update(
                active=active,
                partner_ids=[(6, 0, literal_eval(partner_ids))],
            )
        return res

    def set_values(self):
        self.env["ir.config_parameter"].set_param("college.active", self.active)

        self.env["ir.config_parameter"].set_param(
            "college.partner_ids", self.partner_ids.ids
        )
        return super(Settings, self).set_values()

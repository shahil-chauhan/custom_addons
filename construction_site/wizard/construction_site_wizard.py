# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class ConstructionWizard(models.TransientModel):
    _name = "construction.site.wizard"
    _description = "wizard to print reports between from_date to to_date"

    from_date = fields.Date(string="From_date")
    to_date = fields.Date(string="To_date")

    def print_report(self):
        if self.from_date and self.to_date:
            domain = [
                ("schedule_date", ">=", self.from_date),
                ("schedule_date", "<=", self.to_date),
            ]
        docids = self.env["construction.site"].search(domain).ids
        print("\n\ndocs\n\n", docids)
        return self.env.ref(
            "construction_site.action_construction_site_report"
        ).report_action(docids)

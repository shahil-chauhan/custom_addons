# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def demo_cron(self):
        print("\n\n\n\ncron called------")
        partners = self.search([])
        print("\n\n\n\nPartners------", partners)

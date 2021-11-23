from odoo import api, fields, models


class SaleMailWizard(models.TransientModel):
    _name = "sale.mail.wizard"
    _description = "Sale Mail Wizard"

    name = fields.Char(string="Name")

from odoo import api, fields, models


class CreateWizard(models.TransientModel):
    _name = "create.wizard"
    _description = "Create Wizard"

    name = fields.Char(string="Name")

    def cancel_object(self):

        print("\n\n\n\n\nHello\n\n\n\n\n")

from odoo import fields, models


class documentationVersion(models.Model):
    _name = "docu.version"
    _description = "documentation versions"

    name = fields.Char(string="Version Name")
    active = fields.Boolean(string="Active", default=True)

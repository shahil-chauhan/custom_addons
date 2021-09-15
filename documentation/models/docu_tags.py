from odoo import fields, models


class documentationTags(models.Model):
    _name = "docu.tags"
    _description = "documentation tags"

    name = fields.Char(string="Tag Name")
    color = fields.Integer(string="Color")
    active = fields.Boolean(string="Active", default=True)

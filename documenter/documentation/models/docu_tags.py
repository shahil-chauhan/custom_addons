from odoo import fields, models
from odoo.tools.translate import _


class DocumenterTags(models.Model):
    _name = "docu.tags"
    _description = "Documenter Tags"

    name = fields.Char(string=_("Name"), required=True)
    active = fields.Boolean(default=True)
    color = fields.Integer(string=_("Color Index"), default=0)

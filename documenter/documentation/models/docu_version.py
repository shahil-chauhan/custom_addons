from odoo import fields, models
from odoo.tools.translate import _


class DocumenterVersion(models.Model):
    _name = "docu.version"
    _description = "Documenter Version"

    name = fields.Char(string=_("Name"), required=True)
    active = fields.Boolean(default=True)

# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.tools.translate import _


class ResPartner(models.Model):
    _inherit = "res.partner"

    credit_limit = fields.Boolean(string=_("Credit Limit"))
    blocking_limit = fields.Boolean(string=_("Blocking Limit"))
    credit_limit_score = fields.Float(string=_("Credit Limit Score"))
    blocking_limit_score = fields.Float(string=_("Blocking Limit Score"))

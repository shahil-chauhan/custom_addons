from odoo import api, fields, models
from odoo.tools.translate import _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    surcharge = fields.Float(string=_("One-time surcharge"))
    list_price = fields.Float(string=_("Subscription Price"))

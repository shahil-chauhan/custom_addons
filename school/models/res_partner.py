from odoo import api, fields, models
from odoo.tools.translate import _


class ResPartner(models.Model):
    _inherit = "res.partner"

    # @api.model
    # def _name_search(self, name, city, args=None, operator='ilike', limit=1):
    #     args = args or []
    #     domain  = []
    #     if name:
    #         domain = ['|', ('name',operator,name),('city',operator,city)]
    #     return self._search(args + domain, limit=limit)

    def name_get(self):
        result = []
        for account in self:
            result.append(
                (
                    account.id,
                    "{} ({}) {}".format(
                        account.name,
                        account.city,
                        account.property_supplier_payment_term_id.name,
                    ),
                )
            )
        return result

    @api.model
    def _name_search(self, name, args=None, operator="ilike", limit=None):
        args = args or []
        domain = []
        if name:
            domain = ["|", ("name", operator, name), ("city", operator, name)]
        return self._search(args + domain, limit=1)

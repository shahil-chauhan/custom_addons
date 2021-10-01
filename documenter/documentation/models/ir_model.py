from odoo import api, models
from odoo.osv import expression


class IrModel(models.Model):
    _inherit = "ir.model"

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        if self._context.get("docu_apps"):
            apps = (
                self.env["ir.module.module"]
                .browse(self._context["docu_apps"][0][2])
                .mapped("name")
            )
            ids = []
            for model in self.search([]):
                for app in apps:
                    if model.modules.find(app.split("_")[0]) != -1:
                        ids.append(model.id)
            domain += [("id", "in", ids)]
        return super(IrModel, self).search_read(domain, fields, offset, limit, order)

    @api.model
    def _name_search(
        self, name, args=None, operator="ilike", limit=100, name_get_uid=None
    ):
        args = args or []
        domain = []
        if self._context.get("docu_apps"):
            apps = (
                self.env["ir.module.module"]
                .browse(self._context["docu_apps"][0][2])
                .mapped("name")
            )
            ids = []
            for model in self.search([]):
                for app in apps:
                    if model.modules.find(app.split("_")[0]) != -1:
                        ids.append(model.id)
            domain = [("id", "in", ids)]
        return self._search(
            expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid
        )

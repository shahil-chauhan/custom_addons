from odoo import fields, models
from odoo.tools.translate import _


class ConstructionSite(models.Model):
    _name = "construction.site"
    _description = "Construction site data"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string=_("Name"), required=True, store=True)
    reference = fields.Char(string=_("Reference"), required=True, store=True)
    schedule_date = fields.Datetime(string=_("Schedules Date"))
    state = fields.Selection([
        ("draft", "Draft"),
        ("running", "Running"),
        ("stop", "Stop"),
        ("in_closing", "In closing"),
        ("close", "Closed"),
    ],
        string="Status",
        default="draft", )

    responsible_internal_id = fields.Many2one("hr.employee", string=_("Responsible ID"))
    responsible_on_site_id = fields.Many2one("res.partner", string=_("Responsible"))
    delivery_address = fields.Many2one("res.partner", string=_("Address"))
    product_template_id = fields.Many2one("product.template", string=_("Product"))
    stock_warehouse_id = fields.Many2one("stock.warehouse", string=_("Warehouse"))
    project_id = fields.Many2one("project.project", string=_("Project"))
    purchase_order_ids = fields.Many2many("purchase.order", "pur_ord_tbl", string=_("Purchase Order"))
    analytical_account_id = fields.Many2one("account.analytic.account", string=_("Analytical Account"))
    sale_order_id = fields.Many2one("sale.order", string=_("Sale Order"))
    asset_ids = fields.Many2many("account.asset", "ass_tbl", string=_("Asset"))
    general_contractor_purchase_order_id = fields.Many2one("purchase.order", string=_("General Contractor Purchase"))

    def action_run(self):
        self.state = "running"

    def action_stop(self):
        self.state = "stop"

    def action_in_close(self):
        self.state = "in_closing"

    def action_close(self):
        self.state = "close"

    def action_draft(self):
        self.state = "draft"

    def name_get(self):
        name_list = []
        for name_code in self:
            if name_code.reference:
                display_name = "[{}] {}".format(name_code.reference, name_code.name)
            name_list.append((name_code.id, display_name))
        return name_list

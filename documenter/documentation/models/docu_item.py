from odoo import api, fields, models
from odoo.tools.translate import _


@api.model
def _lang_get(self):
    return self.env["res.lang"].get_installed()


class DocumenterItem(models.Model):
    _name = "docu.item"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Documenter Item"

    name = fields.Char(string=_("Name"), required=True, tracking=True)
    language = fields.Selection(_lang_get, string=_("Language"))
    active_lang_count = fields.Integer(compute="_compute_active_lang_count")
    description_short = fields.Text(string=_("Short Description"), tracking=True)
    description_long = fields.Html(string=_("Long Description"), tracking=True)
    version_id = fields.Many2one(
        "docu.version", string=_("Version"), tracking=True, required=True
    )
    video_url = fields.Char(string=_("Video URL"), tracking=True)
    google_document_url = fields.Char(string=_("Google Doc URL"), tracking=True)
    tags = fields.Many2many(
        "docu.tags",
        "item_tags_relation",
        "item_id",
        "tag_id",
        string=_("Tags"),
        tracking=True,
    )
    item_type = fields.Selection(
        [
            ("documentation", "Documentation"),
            ("tipp", "Tipp"),
            ("customer", "Customer"),
            ("automation", "Automation"),
            ("technical", "Technical"),
            ("configuration", "Configuration"),
        ],
        string=_("Type"),
        tracking=True,
        required=True,
    )
    # apps = fields.Many2many(
    #     "ir.module.module",
    #     string=_("Apps"),
    #     tracking=True,
    #     domain=[("application", "=", True)],
    # )
    # models = fields.Many2many(
    #     "ir.model",
    #     string=_("Models"),
    #     tracking=True,
    # )
    # views = fields.Many2many(
    #     "ir.ui.view",
    #     string=_("Views"),
    #     tracking=True,
    #     domain=[("type", "not in", ["search", "qweb", "cohort", "activity"])],
    # )
    active = fields.Boolean(default=True)

    @api.depends("language")
    def _compute_active_lang_count(self):
        lang_count = len(self.env["res.lang"].get_installed())
        for item in self:
            item.active_lang_count = lang_count

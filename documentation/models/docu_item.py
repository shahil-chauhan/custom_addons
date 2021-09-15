from odoo import api, fields, models


class documentation(models.Model):
    _name = "docu.item"
    _description = "documentation model"

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Title")
    lang_id = fields.Many2one("res.lang", string="Language")
    desc_short = fields.Text(string="Description Short")
    desc_long = fields.Html(string="Description Long")
    module_id = fields.Many2one(
        "ir.module.module", string="Apps", domain=[("application", "=", True)]
    )
    model_id = fields.Many2one("ir.model", string="Models")
    view_id = fields.Many2one("ir.ui.view", string="Views")
    version_id = fields.Many2one("docu.version", string="Version")
    types = fields.Selection(
        [
            ("documentation", "Documentation"),
            ("tipp", "Tipp"),
            ("customer", "Customer"),
            ("automation", "Automation"),
            ("technical", "Technical"),
            ("configuration", "Configuration"),
        ]
    )
    video_url = fields.Char(string="Video URL")
    google_doc_url = fields.Char(string="GoogleDoc URL")
    tag_ids = fields.Many2many(
        "docu.tags", "docu_item_tags_rel", "item_id", "tag_id", string="Tag"
    )

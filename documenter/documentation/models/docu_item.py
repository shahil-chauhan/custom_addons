import re
from urllib.parse import urlparse

from odoo import api, fields, models
from odoo.addons.website.tools import get_video_embed_code
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


@api.model
def _lang_get(self):
    return self.env["res.lang"].get_installed()


class DocumenterItem(models.Model):
    _name = "docu.item"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Documenter Item"

    name = fields.Char(string=_("Title"), required=True, tracking=True)
    language = fields.Selection(_lang_get, string=_("Language"))
    active_lang_count = fields.Integer(compute="_compute_active_lang_count")
    description_short = fields.Text(string=_("Short Description"), tracking=True)
    description_long = fields.Html(string=_("Long Description"), tracking=True)
    version_id = fields.Many2one(
        "docu.version", string=_("Version"), tracking=True, required=True
    )
    video_url = fields.Char(string=_("Video URL"), tracking=True)
    embed_code = fields.Char(compute="_compute_embed_code")
    google_document_url = fields.Char(string=_("Google Doc URL"), tracking=True)
    doc_embed_code = fields.Char(compute="_compute_doc_embed_code")
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
    apps = fields.Many2many(
        "ir.module.module",
        string=_("Apps"),
        tracking=True,
        domain=[("application", "=", True)],
    )
    models = fields.Many2many(
        "ir.model",
        string=_("Models"),
        tracking=True,
    )
    views = fields.Many2many(
        "docu.item.view",
        string=_("Views"),
        tracking=True,
    )
    active = fields.Boolean(default=True)
    partner_id = fields.Many2one(
        "res.partner",
        default=lambda self: self.env.user.partner_id,
        string=_("Customer"),
    )

    @api.depends("language")
    def _compute_active_lang_count(self):
        lang_count = len(self.env["res.lang"].get_installed())
        for item in self:
            item.active_lang_count = lang_count

    @api.depends("video_url")
    def _compute_embed_code(self):
        for item in self:
            item.embed_code = get_video_embed_code(item.video_url)

    @api.depends("google_document_url")
    def _compute_doc_embed_code(self):
        for item in self:
            url = item.google_document_url
            if url:
                parsed = urlparse(url)
                if not (
                    parsed.netloc == "docs.google.com"
                    and (parsed.scheme == "http" or parsed.scheme == "https")
                ):
                    raise ValidationError(
                        _("Provided doc URL is not valid. Please enter a valid URL.")
                    )
                if re.search(r"(pub|embedded=true)+$", url):
                    url = url + (
                        "?embedded=true" if not url.endswith("?embedded=true") else ""
                    )
                    item.doc_embed_code = (
                        '<iframe class="embed-responsive-item" src="%s" frameborder="0" height="150"></iframe>'  # noqa: E501
                        % url
                    )
                else:
                    item.doc_embed_code = (
                        '<iframe class="embed-responsive-item" src="%s/preview" frameborder="0" height="150"></iframe>'  # noqa: E501
                        % url[: url.rfind("/")]
                    )
            else:
                item.doc_embed_code = ""

    @api.constrains("video_url")
    def _check_valid_video_url(self):
        for item in self:
            if item.video_url and not item.embed_code:
                raise ValidationError(
                    _(
                        "Provided video URL is not valid. Please enter a valid video URL."
                    )
                )


class DocumenterItemView(models.Model):
    _name = "docu.item.view"
    _description = "Documenter Views"

    name = fields.Char(required=True, string=_("Name"))
    view_type = fields.Char()

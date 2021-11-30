from odoo import _, fields, models


class Settings(models.TransientModel):
    _inherit = "res.config.settings"

    notify_person = fields.Char(
        string=_("Notify Person for Limit Exceed"),
        config_parameter="credit_block_limit.notify_person",
    )

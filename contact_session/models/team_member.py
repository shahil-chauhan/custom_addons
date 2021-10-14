from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


class TeamMember(models.Model):
    _name = "team.member"
    _description = "Contains the details of the team members under tl"

    name = fields.Char(related="member_id.name", string=_("Name"))
    email = fields.Char(related="member_id.email", string=_("Email"))
    phone = fields.Char(related="member_id.phone", string=_("Phone"))
    address = fields.Char(related="member_id.contact_address", string=_("Address"))

    partner_id = fields.Many2one("res.partner", string=_("Contact"))
    member_id = fields.Many2one(
        "res.partner", domain="[('team_lead', '=', False)]", string=_("Member")
    )

    class Team(models.Model):
        _inherit = "res.partner"

        team_lead = fields.Boolean(string=_("Team lead"))
        team_lead_ids = fields.One2many(
            "team.member", "partner_id", string=_("Team member")
        )

from odoo import fields, models, api
from odoo.tools.translate import _


class TeamMember(models.Model):
    _name = "team.member"
    _description = "bla bla bla..."

    contact_id = fields.Many2one("res.partner", domain="[('team_lead', '=', False)]", string=_("Contact"))


class Team(models.Model):
    _inherit = "res.partner"

    team_lead = fields.Boolean(string=_("team lead"))
    team_lead_ids = fields.One2many("team.member", "contact_id", string=_("team member"))

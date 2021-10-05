from odoo import fields, models, api
from odoo.tools.translate import _


class TeamMember(models.Model):
    _name = "team.member"

    team_lead = fields.Boolean(string="_(team lead)")
    contact_id = fields.Many2one("res.partner", string="_(contact)")


class Team(models.Model):
    _inherit = "res.partner"

    team_lead_ids = fields.One2many(
        "team.member", "contact_id", string="_(team member)")

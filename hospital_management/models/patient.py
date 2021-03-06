from odoo import _, api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "patient records"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "patient_name"

    patient_name = fields.Char(string="Patient Name", required=True, tracking=True)
    ref = fields.Char(
        string="Patient Reference",
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _("New"),
    )
    patient_age = fields.Integer(string="Patient Age", tracking=True)
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("other", "Other")],
        required=True,
        default="male",
    )

    reference_id = fields.Many2one("res.partner", string="Reference")
    note = fields.Text(string="Notes")
    photo = fields.Binary(string="Photo")

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirm", "Confirmed"),
            ("done", "Done"),
            ("cancel", "Cancelled"),
        ],
        string="Status",
        default="draft",
    )

    def action_confirm(self):
        self.state = "confirm"

    def action_done(self):
        self.state = "done"

    def action_cancel(self):
        self.state = "cancel"

    def action_draft(self):
        self.state = "draft"

    @api.model
    def create(self, values):
        if not values.get("note"):
            values["note"] = "New Patient"

        # ----TO PRINT THE SEQUENCE VALUE-----
        if values.get("ref", _("New")) == _("New"):
            values["ref"] = self.env["ir.sequence"].next_by_code(
                "hospital.patient"
            ) or _("New")

        print(
            "\n\n\n Create Override----",
        )
        rtn = super(HospitalPatient, self).create(values)
        print("\n\n\n values---", values)
        print("\n\n\n Return---", rtn)
        return rtn

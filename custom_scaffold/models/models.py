from odoo import _, api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "patient records"

    patient_name = fields.Char(string="Patient Name", required=True, tracking=True)
    reference_id = fields.Many2one("res.partner", string="Reference")
    state = fields.Selection([("draft", "Draft")], string="Status", default="draft")

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

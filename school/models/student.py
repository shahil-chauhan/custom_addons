from odoo import api, fields, models


class StudentProfile(models.Model):
    _name = "student.profile"
    _description = "Student Information"

    @api.depends("is_parking")
    def _compute_total_calcu(self):
        for rec in self:
            if rec.is_parking == True:
                rec.calculate = 50
            elif rec.is_parking == False:
                rec.calculate = 100

    name = fields.Char(string="Student name")
    student_email = fields.Char(string="Email")
    student_phone = fields.Char(string="Phone")
    student_result = fields.Float(string="Result")
    student_img = fields.Image(
        string=" Upload student image", max_width=100, max_height=100
    )
    school_select_id = fields.Many2one("school.profile", string="Select School")
    sc_select_id = fields.Many2many("school.profile", string="Selectssss")
    # sc_select_id = fields.One2many("school.profile", string="Selectssss")
    user_signature = fields.Binary(string="Signature")
    is_parking = fields.Boolean(
        related="school_select_id.parking", string="Is parking", store=True
    )
    calculate = fields.Integer(compute="_compute_total_calcu", string="Calculate")
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirm", "Confirm"),
            ("done", "Done"),
            ("cancel", "Cancel"),
        ],
        default="draft",
        string="Status",
    )

    def test(self):
        return "Akash"

    @api.model_create_multi  # or   @api.model
    def create(self, vals):
        rtn = super(StudentProfile, self).create(vals)
        return rtn

    def write(self, vals):
        rtn = super(StudentProfile, self).write(vals)
        return rtn

    def unlink(self):
        rtn = super(StudentProfile, self).unlink()
        print("\n\n\nrtn", rtn)
        return rtn

    def copy(self, default={}):
        default["name"] = "copy(" + self.name + ")"
        print("\n\n\nself data", self)
        rtn = super(StudentProfile, self).copy(default=default)
        print("\n\n\nrtn", rtn)
        return rtn

    @api.model
    def default_get(self, field_list=[]):
        print("\n\n\nfiled List", field_list)
        rtn = super(StudentProfile, self).default_get(field_list)
        print("\n\n\nbefore  Edit", rtn)
        # rtn['name'] = "Qqqqq"
        print("\n\n\nAfter  Edit", rtn)
        return rtn

    def fields_view_get(
        self, view_id=None, view_type="form", toolbar=False, submenu=False
    ):
        print("\n\n\nView Id", view_id)
        print("\n\n\nView Type", view_type)
        print("\n\n\nToolbar", toolbar)
        print("\n\n\nSubmenu", submenu)
        rtn = super(StudentProfile, self).fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu
        )
        print("\n\n\nReturn Disc", rtn)
        return rtn

    def action_confirm(self):
        self.state = "confirm"

    def action_done(self):
        self.state = "done"

    def action_cancel(self):
        self.state = "cancel"

    def action_reset(self):
        self.state = "draft"

    def clear_record_data(self):
        self.write(
            {
                "name": "",
                "student_email": "",
                "student_phone": "",
                "student_result": "",
                "student_img": "",
                "user_signature": "",
                "is_parking": "",
                "calculate": "",
            }
        )

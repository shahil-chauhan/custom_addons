from odoo import api, fields, models


class CollegeProfile(models.Model):
    _name = "college.profile"
    _description = "College Management for students"

    name = fields.Char(string="College Name")
    email = fields.Char(string="Email ID")
    phone = fields.Char(string="Phone")
    is_virtual_class = fields.Boolean(string="Virtual Classes")
    college_rank = fields.Integer(string="Rank")
    result = fields.Float(string="Result")
    address = fields.Text(string="Address")
    establish_date = fields.Date(string="Establish Date")
    open_date = fields.Datetime("Open Date")
    college_type = fields.Selection(
        [("public", "Public College"), ("private", "Private College")],
        string="Type of College",
    )
    image = fields.Binary(string="College Image")

    student_ids = fields.One2many(
        "student.profile", "college_id", string="Students List"
    )

    auto_rank = fields.Integer(
        compute="auto_rank_result", string="Auto Rank", store=True
    )

    @api.depends("college_type")
    def auto_rank_result(self):
        for rec in self:
            if rec.college_type == "private":
                rec.auto_rank = 50
            elif rec.college_type == "public":
                rec.auto_rank = 100
            else:
                rec.auto_rank = 0

    # document = fields.Binary(string="Document")
    # document_name = fields.Char(string="Document_name")

    # college_description = fields.Html(string="Description")

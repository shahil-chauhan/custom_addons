from odoo import fields, models, api


class Student(models.Model):
    _name = "student.profile"
    _description = "Student Management"

    name = fields.Char(string="Student Name", required=True)
    enroll = fields.Char("Enrollment No.", required=True)
    department = fields.Char(string="Department")
    semester = fields.Selection(
        [
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5"),
            ("6", "6"),
            ("7", "7"),
            ("8", "8"),
        ],
        string="Semester",
    )
    dob = fields.Date("Date of Birth")
    phone = fields.Char("Mobile No.", size=10)
    image = fields.Binary(string="image")
    college_id = fields.Many2one("college.profile", string="College")
    hobby_list = fields.Many2many(
        "hobby", "student_hobby_rel", "student_id", "hobby_id", string="Hobbies"
    )

    is_virtual = fields.Boolean(
        related="college_id.is_virtual_class", string="Is Virtual"
    )

    currency_id = fields.Many2one("res.currency", string="Currency")
    student_fees = fields.Monetary(string="School Fees")
    active = fields.Boolean(string="Active")

    @api.model 
    def create(self, values):
        print("\n\n\nvalues----",values)
        print("\n\n\nself----",self)
        values['active'] = True
        rtn = super(Student, self).create(values)
        print("\n\n\nreturned----",rtn)
        return rtn


class Hobby(models.Model):
    _name = "hobby"
    _description = "Different hobbies of Students"
    name = fields.Char(string="Hobby")

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SchoolProfile(models.Model):
    _name = "school.profile"
    _description = "School Information"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    # _rec_name = "name"

    name = fields.Char(
        string="School name",
        help="Write a school name",
        index=True,
    )
    type = fields.Selection(
        [("public", "Public"), ("private", "Private")], string="Type"
    )
    email = fields.Char(string="Email", default="xyz@gmail.com")

    phone = fields.Char(string="Phone")

    parking = fields.Boolean(string="Parking")
    result = fields.Float(string="Result")
    fees = fields.Integer(string="Fees")
    salary = fields.Integer(
        compute="_compute_course_wise_salary",
        string="Salary",
        readonly=True,
        store=True,
    )
    school_address = fields.Text(string="School address")
    establish_date = fields.Date(string="Establish date")
    open_date = fields.Datetime(string="open date")
    courses = fields.Selection(
        [
            ("computer", "Computer"),
            ("automobile", "Auto Mobile"),
            ("civil", "Civil"),
            ("mechanical", "Mechanical"),
            ("electrical", "Electrical"),
        ],
        string="Course selection",
    )
    documents = fields.Binary(string="Documents")
    docu_name = fields.Char(string="Documents name")
    image = fields.Binary(attachment=True, store=True)
    image_name = fields.Char(string="Image Name", invisible="1")
    school_desc = fields.Html(string="School description")
    student_data_ids = fields.One2many(
        "student.profile", "school_select_id", string="Student data"
    )
    # student_data_id = fields.Many2one('student.profile', string='Studeadfasdnt data')
    delivery_count = fields.Integer(
        string="Delivery Orders", compute="_compute_picking_ids"
    )
    total_student_count = fields.Integer(
        string="Total Student", compute="_compute_count_total_student"
    )
    seq = fields.Integer(default=1)

    # @api.depends('total_student_count')
    # def _compute_count_total_student(self):
    #     stu = self.env['student.profile'].search_count([])
    #     total = len(stu)
    #     print("\n\n\n\n", total, "\n\n\n\n\n")

    @api.depends("courses")
    def _compute_course_wise_salary(self):
        for cor in self:
            if cor.courses == "computer":
                cor.salary = 280000
            elif cor.courses == "electrical":
                cor.salary = 30000
            elif cor.courses == "automobile":
                cor.salary = 32000
            elif cor.courses == "civil":
                cor.salary = 27000
            else:
                cor.salary = 10000

    def button_on_click(self):
        print("smart button click")

    @api.depends("delivery_count")
    def _compute_picking_ids(self):
        for stud in self:
            stud.delivery_count = self.env["student.profile"].search_count(
                [("school_select_id.id", "=", self.id)]
            )

    def button_click(self):
        print("smart button click")
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "student",
            "view_mode": "tree",
            "res_model": "student.profile",
            "domain": [("school_select_id.id", "=", self.id)],
        }

    # @api.model
    # def name_create(self, name):
    #     print("name_create calling...", name)
    #     rtn = super(StudentProfile, self).name_create(name)
    #     return rtn

    # def name_create(self, name):
    #     print("\n\nself", self)
    #     print("\n\nSchool name", name)
    #     rtn = self.create({'name': name,'email':'addd@gmail.com'})
    #     print("\n\nrtn", rtn)
    #     print("\n\nrtn.name_get()[0]", rtn.name_get()[0])
    #     return rtn.name_get()[0]

    # def name_get(self):
    #     student_list = []
    #     print("\n\n\nstudent list",student_list)
    #     for school in self:
    #         print("Type of school", type(school.type))
    #
    #         print("school",school)
    #         if school.type:
    #             print("Type of school",type(school.type))
    #             name = school.name + " " + school.type
    #         # name = school.name + " " + str(school.type)
    #             print("School name",school.name)
    #             print("name",name,"\n\n\n")
    #             student_list.append((school.id,name))
    #     return student_list
    def temp(self):
        dic = {"y": "yashu"}
        return dic

    def wiz_open(self):
        return self.env["ir.actions.act_window"]._for_xml_id(
            "school.action_create_wizard"
        )

    def school_send_mail(self):
        print("\n\n\n\n\n\nstudenttttttttt")
        template = self.env.ref("school.school_mail_template_view")
        print("\n\n\n\n\n\nstudenttttttttt")
        template.send_mail(self.id)


# return {'type': "ir.actions.act_window",
#         'res_model': "create.wizard",
#         'view_mode': "form",
#         'target': "new"}


class TestMethod(models.Model):
    _name = "report.sale.report_saleorder_document"
    _description = "bako"


# def temp(self):
# 	dic = {'y': 'yashu'}
# 	return dic

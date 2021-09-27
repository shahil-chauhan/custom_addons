from lxml import etree
import  random
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

    # compute method to calculate 
    @api.depends("college_type")
    def auto_rank_result(self):
        for rec in self:
            if rec.college_type == "private":
                rec.auto_rank = 50
            elif rec.college_type == "public":
                rec.auto_rank = 100
            else:
                rec.auto_rank = 0

    # name_create method to create a record with name field.
    @api.model
    def name_create(self, name):
        # rtn = self.create({'name':name})
        # return rtn.name_get()[0]
        print("\n\nself--- ", self)
        print("\n\nname----", name)
        rtn = super(CollegeProfile, self).name_create(name)
        print("\n\nname create return-----", rtn)
        return rtn

    # name_get() method to return records textual value
    def name_get(self):
        college_list = []
        for college in self:
            name = college.name
            if college.college_type:
                name += " ({})".format(college.college_type)
            college_list.append((college.id, name))
        return college_list

    # name_search method to return list of pairs based on filters
    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or []
        print("\n\nName=", name)
        print("\n\nArgs=", args)
        print("\n\noperator=", operator)
        print("\n\nLimit=", limit)
        if name:
            rec = self.search(['|',('name',operator,name),('college_type',operator,name)])
            return rec.name_get()
        return self.search([('name', operator,name)]+args, limit=limit).name_get()


    # document = fields.Binary(string="Document")
    # document_name = fields.Char(string="Document_name")
    # college_description = fields.Html(string="Description")


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
    student_fees = fields.Monetary(string="School Fees", default=2000.00)
    active = fields.Boolean(string="Active")

    def custom_button_method(self):

        # to add fields data through raw sql commands
        self.env.cr.execute("insert into school_profile(name, active) values('From button click', True)")
        self.env.cr.commit()

        # different methods releted to the environment
        print("\nEnvi------", self.env) 
        print("\nuser id------", self.env.uid) 
        print("\nCurrent user------", self.env.user) 
        print("\nSuper------", self.env.su) 
        print("\nCompany------", self.env.company)
        print("\nComapnies------", self.env.companies)
        print("\nLang------", self.env.lang)
        print("\nCursor------", self.env.cr)

        print("Hello I am a custom button method")
        self.student_fees = random.randint(1,1000)

    # # Create method to create new record
    # @api.model
    # def create(self, values):
    #     print("\n\n\nvalues----", values)
    #     print("\n\n\nself----", self)
    #     # to set the value of active field while overriding create method.
    #     values['active'] = True
    #     rtn = super(Student, self).create(values)
    #     print("\n\n\ncreate returned----", rtn)
    #     return rtn

    # # write method to update an exist record
    # # NO Decorator
    # def write(self, vals):
    #     print("\n\n\nself----", self)
    #     print("\n\nValues-----", vals)
    #     # vals['active'] = True #to update the value of active field while overriding write method.
    #     rtn = super(Student, self).write(vals)
    #     print("\n\nwrite Return-----", rtn)
    #     return rtn

    # # copy method to create new record from existing record
    # def copy(self, default=None):
    #     print("\n\n\nself----", self)
    #     # default['active'] = False # copy with active field false
    #     rtn = super(Student, self).copy(default=default)
    #     print("\n\ncopy Return-----", rtn)
    #     return rtn

    # # unlink method to delete a record
    # def unlink(self):
    #     print("\n\n\nself----", self)
    #     # you can write your condition for unlink
    #     rtn = super(Student, self).unlink()
    #     print("\n\nunlink Return-----", rtn)
    #     return rtn

    # # default_get method to set default values while creating records
    # def default_get(self, fields_list=[]):
    #     print("\n\nself---", self)
    #     print("\n\nField list---", fields_list)
    #     rtn = super(Student, self).default_get(fields_list)
    #     rtn['is_virtual'] = True
    #     print("\n\ndefault_get ---", rtn)
    #     return rtn

    # fields_view_get() method to return specific viewtype in dict format
    def fields_view_get(self, view_id=None, view_type="form", toolbar=False, submenu=False):
        # print("\n\nView_id--", view_id)
        # print("\n\nView_type--", view_type)
        # print("\n\nToolbar--", toolbar)
        # print("\n\nsubmneu--", submenu)
        rtn = super(Student, self).fields_view_get(
            view_id=view_id, view_type=view_type, submenu=submenu, toolbar=toolbar
        )
        if view_type == "form":
            doc = etree.XML(rtn["arch"])
            name_field = doc.xpath("//field[@name='name']")
            if name_field:
                # added one label in form view
                name_field[0].addnext(
                    etree.Element("label", {"string": "hello fields_view_get method"})
                )
                rtn["arch"] = etree.tostring(doc, encoding="unicode")

        # print("\n\nFields_view_get--", rtn)
        return rtn


class Hobby(models.Model):
    _name = "hobby"
    _description = "Different hobbies of Students"
    name = fields.Char(string="Hobby")

    # name_create method to create a record with name field.
    @api.model
    def name_create(self, name):
        # rtn = self.create({'name':name})
        # return rtn.name_get()[0]
        print("\n\nself--- ", self)
        print("\n\nname----", name)
        rtn = super(Hobby, self).name_create(name)
        print("\n\nname create return-----", rtn)
        return rtn

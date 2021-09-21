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
    student_fees = fields.Monetary(string="School Fees", default=2000.00)
    active = fields.Boolean(string="Active")

    # Create method to create new record
        # @api.model
        # def create(self, values):
        #     print("\n\n\nvalues----", values)
        #     print("\n\n\nself----", self)
        #     # to set the value of active field while overriding create method.
        #     values['active'] = True
        #     rtn = super(Student, self).create(values)
        #     print("\n\n\ncreate returned----", rtn)
        #     return rtn

    # write method to update an exist record
    # NO Decorator
    def write(self, vals):
        print("\n\n\nself----", self)
        print("\n\nValues-----", vals)
        # vals['active'] = True #to update the value of active field while overriding write method.
        rtn = super(Student, self).write(vals)
        print("\n\nwrite Return-----", rtn)
        return rtn

    # copy method to create new record from existing record
    def copy(self, default=None):
        print("\n\n\nself----", self)
        # default['active'] = False # copy with active field false
        rtn = super(Student, self).copy(default=default)
        print("\n\ncopy Return-----", rtn)
        return rtn

    # unlink method to delete a record
    def unlink(self):
        print("\n\n\nself----", self)
        # you can write your condition for unlink
        rtn = super(Student, self).unlink()
        print("\n\nunlink Return-----", rtn)
        return rtn

    # default_get method to set default values while creating records
    def default_get(self, fields_list=[]):
        print("\n\nself---",self)
        print("\n\nField list---",fields_list)
        rtn = super(Student, self).default_get(fields_list)
        rtn['is_virtual'] = True
        print("\n\ndefault_get ---", rtn)
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

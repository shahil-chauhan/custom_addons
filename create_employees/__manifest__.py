# -*- coding: utf-8 -*-
{
    "name": "Create Employees",
    "summary": """""",
    "author": "Shahil Chauhan",
    'category': 'Generic Modules/Tools',
    "version": "14.0.1.0.0",
    "depends": ['base','hr_recruitment', 'website'],
    "data": [
        "security/ir.model.access.csv",
        "security/create_employee_security.xml",
        "data/employees_menu.xml",
        "views/create_employee_view.xml",
        "views/create_employee_template.xml",
        "views/employee_details_template.xml",
        "views/hr_job_inherit.xml",
    ],

    "installable": True,
    "application": True,
    "auto_install": False,
    "sequence": 1,
}

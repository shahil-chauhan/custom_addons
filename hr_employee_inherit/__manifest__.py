# -*- coding: utf-8 -*-
{
    "name": "HR Employee Inherit",
    "version": "14.0.1.0.0",
    "author": "Shahil Chauhan",
    "sequence": 1,
    "category": "Generic Modules/Tools",
    "description": """
        Sequence Creation and wizard

    """,
    "summary": "HR Employee Inherit",
    "depends": ["base", "hr"],
    "data": [
        "security/ir.model.access.csv",
        "data/seq_data.xml",
        "views/hr_employee_form_inherit.xml",
        "wizard/hr_employee_wizard _view.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}

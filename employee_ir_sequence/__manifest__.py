# -*- coding: utf-8 -*-

{
    "name": "HR Employee Sequence",
    "version": "14.0.1.0.0",
    "author": "Yash Shah",
    "category": "Generic Modules/Tools",
    "description": """This module will demonstrate how to generate ir sequence and create wizard""",
    "summary": "HR Employee IR Sequence",
    "depends": ["base", "hr"],
    "data": [
        "security/ir.model.access.csv",
        "data/sequence_view.xml",
        "views/employee_seq_view.xml",
        "wizard/wizard_view.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "sequence": 1,
}

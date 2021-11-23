# -*- coding: utf-8 -*-
{
    "name": "",
    "summary": """
        """,
    "description": """
    """,
    "author": "Shahil Chauhan",
    "website": "http://www.yourcompany.com",
    "category": "Uncategorized",
    "version": "14.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/views.xml",
        "views/templates.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "application": True,
    "installable": True,
    "auto_install": False,
    "sequence": 1,
}

# -*- coding: utf-8 -*-
{
    "name": "Contact Session",
    "summary": """
         Module for Contact display session""",
    "author": "Shahil Chauhan",
    "version": "14.0.1.0.0",
    "depends": ["website", "contacts"],
    "data": [
        "security/ir.model.access.csv",
        "data/contact_menu.xml",
        "views/contact_form_inherit.xml",
        "views/contact_view.xml",
        "views/assets.xml",
        "views/contacts_list.xml",
        "views/contact_detail.xml",
    ],
    "auto_install": False,
    "installable": True,
    "application": True,
}

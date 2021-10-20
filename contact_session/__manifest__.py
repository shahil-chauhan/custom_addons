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
        "views/assets.xml",
        "views/contact_form_inherit.xml",
        "views/team_member_tree_view.xml",
        "views/contacts_list_template.xml",
        "views/contact_details_template.xml",
        "views/contact_create_template.xml",
        "views/error_dialog_template.xml",
    ],
    "auto_install": False,
    "installable": True,
    "application": True,
}

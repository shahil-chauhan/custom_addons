# -*- coding: utf-8 -*-
{
    "name": "Credit/Blocking Limit",
    "summary": """ Add customer credit and blocking limits
        """,
    "description": """ A module to add the customer credit and blocking limits for sales/quotations creation.
    """,
    "author": "Shahil Chauhan",
    "category": "sale",
    "website": "http://www.aktivsoftware.com",
    "version": "14.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": ["sale_management", "website"],
    # always loaded
    "data": [
        "data/partner_info_menu.xml",
        "data/limit_mail_template.xml",
        "views/assets.xml",
        "views/res_partner_views.xml",
        "views/res_partner_setting.xml",
        "views/partner_info_template.xml",
        "views/partner_form_template.xml",
        "views/partner_updated_template.xml",
    ],
    # only loaded in demonstration mode
    "application": True,
    "installable": True,
    "auto_install": False,
    "sequence": 1,
}

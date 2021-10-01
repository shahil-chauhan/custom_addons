# -*- coding: utf-8 -*-

{
    "name": "Documentation",
    "summary": """""",
    "description": """""",
    "author": "much. GmbH",
    "website": "https://muchconsulting.de",
    # for the full list
    "category": "",
    "version": "14.0.1.1.0",
    # any module necessary for this one to work correctly
    "depends": [
        "crm",
        "sale_management",
        "website_sale",
    ],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "data/docu_version_data.xml",
        "data/view_type_data.xml",
        "data/documentation_items.xml",
        "views/docu_item_views.xml",
        "views/docu_tags_views.xml",
        "views/docu_version_views.xml",
        "views/menuitems.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}

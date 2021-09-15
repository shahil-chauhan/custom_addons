# -*- coding: utf-8 -*-

{
    "name": "Documentation1",
    "summary": """""",
    "description": """""",
    "author": "much. GmbH",
    "website": "https://muchconsulting.de",
    # for the full list
    "category": "",
    "version": "14.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "mail",
    ],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "data/docu_version_data.xml",
        "views/docu_item_views.xml",
        "views/docu_tags_views.xml",
        "views/docu_version_views.xml",
        "views/menuitems.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}

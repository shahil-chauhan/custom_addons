# -*- coding: utf-8 -*-

{
    "name": "Help Icon",
    "summary": """""",
    "description": """""",
    "author": "much. GmbH",
    "website": "https://muchconsulting.de",
    # for the full list
    "category": "",
    "version": "14.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": [
        "documentation",
    ],
    # always loaded
    "data": [
        "views/assets.xml",
    ],
    "qweb": ["static/src/xml/systray_help_menu.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
}

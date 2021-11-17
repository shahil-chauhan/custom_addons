# -*- coding: utf-8 -*-
{
    "name": "Construction site",
    "summary": """
        Module for Construction site""",
    "description": """
        This module is used to manage the different tasks on the construction site""",
    "author": "Shahil Chauhan",
    "version": "14.0.1.0.0",
    "category": "Construction",
    "website": "https://www.google.com/",
    "depends": [
        "sale_management",
        "account",
        "hr",
        "stock",
        "project",
        "purchase",
        "website",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/construction_site_view.xml",
        "views/construction_portal_templates.xml",
        "views/purchase_order_inherit_view.xml",
        "views/sale_order_inherit_view.xml",
        "views/project_task_inherit_view.xml",
        "wizard/construction_site_wizard_view.xml",
        "report/construction_site_report.xml",
    ],
    "auto_install": False,
    "installable": True,
    "application": True,
}

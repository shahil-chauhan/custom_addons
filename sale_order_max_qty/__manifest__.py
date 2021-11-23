{
    "name": "Project Management",
    "version": "14.0.1.0.0",
    "category": "Testing",
    "summary": "Project management system",
    "sequence": 1,
    "website": "https://www.aktivesoftware.com/",
    "description": "This module gives a framework project management",
    "depends": [
        "sale_management",
        "purchase",
    ],
    "data": [
        "views/product_views.xml",
        "views/sale_views.xml",
        "report/sale_order_inherit_report.xml",
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
    "application": True,
}

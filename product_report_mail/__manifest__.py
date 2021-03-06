{
    "name": "Product Report Mail",
    "version": "14.0.1.0.0",
    "category": "Product",
    "summary": "Product Report management system",
    "sequence": 1,
    "website": "https://www.aktivesoftware.com/",
    "description": "Inherit report and create mail in Product",
    "depends": ["sale_management", "stock"],
    "data": [
        "security/ir.model.access.csv",
        # "wizard/email_wizard_views.xml",
        "report/product_inherit_report_views.xml",
        "views/sale_order_inherit_views.xml",
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
    "application": True,
}

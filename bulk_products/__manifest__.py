# -*- coding: utf-8 -*-
{
    "name": "Bulk Products",
    "summary": """
    to use the bulk product
        """,
    "description": """
    """,
    "author": "Shahil Chauhan",
    "website": "http://www.yourcompany.com",
    "category": "Uncategorized",
    "version": "14.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": ["sale_management", "stock", "website"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "data/bulk_product_website_menu.xml",
        "views/bulk_products_views.xml",
        "views/menu_item_views.xml",
        "views/sales_order_bulk_product_views.xml",
        "views/bulk_product_template.xml",
        "views/form_submit_template.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "application": True,
    "installable": True,
    "auto_install": False,
    "sequence": 1,
}

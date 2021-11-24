# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Bulk Product",
    "version": "14.0.1.0.0",
    "summary": "products and contacts",
    "description": """
====================
    Creating bulk products.
    """,
    "category": "sale/product",
    "depends": [
        "sale_management",
        "website",
        "stock",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/bulk_product_website_menu_views.xml",
        "views/bulk_product_views.xml",
        "views/menu_item_views.xml",
        "views/sale_order_bulk_product_views.xml",
        "views/bulk_product_template.xml",
        "views/submit_success_template.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}

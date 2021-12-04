# -*- coding: utf-8 -*-
{
    "name": "Sale Commission",
    "summary": """ Calculate commission 
        """,
    "description": """Calculate the commission on a product in the sale order line based on the commission in the sale order.
    """,
    "author": "Shahil Chauhan",
    "category": "Sales",
    "version": "14.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": ["sale_management"],
    # always loaded
    "data": [
        "views/sale_order_views.xml",
        "views/res_partner_views.xml",
    ],
    # only loaded in demonstration mode
    "application": True,
    "installable": True,
    "auto_install": False,
    "sequence": 1,
}

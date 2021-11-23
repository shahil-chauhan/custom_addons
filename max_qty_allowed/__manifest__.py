{
    "name": "Order",
    "author": "Yash Shah",
    "summary": """This is task 2""",
    "description": """inherit sale order module""",
    "website": "https://www.youtube.com",
    "category": "Business",
    "version": "14.0.1.0.0",
    "depends": ["sale_management"],
    "data": [
        "views/product_variant_views.xml",
        "views/sale_order_views.xml",
        "report/report.xml",
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
    "sequence": 1,
}

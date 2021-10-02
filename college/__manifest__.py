{
    "name": "College",
    "version": "14.0.1.0.0",
    "summary": "College Management System",
    "sequence": 1,
    "description": "This is a college management system.",
    "category": "Education/College",
    "author": "Shahil Chauhan",
    "website": "https://www.google.com/",
    "depends": ["sale"],
    "data": [
        "security/ir.model.access.csv",
        "data/seq_data.xml",
        "data/college_data.xml",
        "views/college_view.xml",
        "views/sales_inherited.xml",
        "report/student_report.xml",
        "report/college_details_report.xml",
        "report/sale_order_inherit_report.xml",
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
}

{
    "name": "Hr Application",
    "summary": """
       Practical Task""",
    "description": """ Practical Task """,
    "author": "Komal Jimudiya",
    "website": "http://www.yourcompany.com",
    "category": "Business",
    "version": "14.0.1.0.0",
    "depends": ["base", "hr_recruitment", "website"],
    "data": [
        "security/ir.model.access.csv",
        "data/hr_referral_menu.xml",
        "views/hr_referral_application.xml",
        "views/hr_referral_application_template.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
    "sequence": 2,
}

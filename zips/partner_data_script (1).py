url = "http://127.0.0.1:8080"
db = "partner_script"
username = "admin"
password = "admin"

import csv
import os
import xmlrpc.client
from datetime import datetime

common = xmlrpc.client.ServerProxy("%s/xmlrpc/2/common" % url)
version = common.version()
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy("{}/xmlrpc/2/object".format(url))

start_time = datetime.now()
with open(
    "/home/admin123/Aarti/workspace/custom_addons/partner_odoo_script/res.partner.csv",
    newline="",
) as csv_file:
    csv_file = csv.DictReader(csv_file)
    excel_row = 2
    for row in csv_file:
        rec = dict(row)
        if excel_row >= 2:
            partner_id = models.execute_kw(
                db,
                uid,
                password,
                "res.partner",
                "search",
                [[["email", "=", rec["email"].strip()]]],
            )

            if rec["company_id"] == "My Company (San Francisco)":
                country_id = models.execute_kw(
                    db,
                    uid,
                    password,
                    "res.country",
                    "search",
                    [[["name", "=", rec["country_id"]]]],
                )
                models.execute_kw(
                    db,
                    uid,
                    password,
                    "res.partner",
                    "write",
                    [[partner_id[0]], {"country_id": country_id[0]}],
                )

            if rec["country_id"] == "Berlin":
                models.execute_kw(
                    db, uid, password, "res.partner", "unlink", [[partner_id[0]]]
                )

            vals = {
                "name": rec["name"].strip(),
                "phone": rec["phone"].strip(),
                "email": rec["email"].strip(),
                "city": rec["city"].strip(),
            }
            if not partner_id:
                partner_id = models.execute_kw(
                    db, uid, password, "res.partner", "create", [vals]
                )
            else:
                partner_id = models.execute_kw(
                    db, uid, password, "res.partner", "write", [[partner_id[0]], vals]
                )
            excel_row += 1

"""count of partners"""
count_partner_id = models.execute_kw(
    db, uid, password, "res.partner", "search_count", [[]]
)
print("====count_partner_id==", count_partner_id)

print(":::::::::::::start::::::::::", start_time)
print("::::::End Time:::::::::", datetime.now())

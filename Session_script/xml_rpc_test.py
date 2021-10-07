url = "https://127.0.0.1:7014"  # url:url of where odoo service is running
db = "sale_discount_limit_v14"  # db: db which is defined in odoo service
username = (
    "admin"  # username : username through which we will login in db and make changes
)
password = "admin"  # password: password of user name

import csv  # Imported to read csv files
import os
import xmlrpc.client  # import to user xmlrpc API
from datetime import datetime

common = xmlrpc.client.ServerProxy("%s/xmlrpc/2/common" % url)  # for authentication
version = common.version()  # to check if connection is correct before authentication
uid = common.authenticate(
    db, username, password, {}
)  # Used as parameter while calling methods
models = xmlrpc.client.ServerProxy(
    "{}/xmlrpc/2/object".format(url)
)  # Used as parameter while calling method

start_time = datetime.now()

with open("/home/odoo/Downloads/product_template.csv", newline="") as csv_file:
    csv_file = csv.DictReader(csv_file)
    """We use this variable for us while executing csv or excel file in xmlrc
    to know how many records are updated or inserted or if
    scripts stops its execution due to any reasons at that time we can get the
    row number of xls or csv file at which row script stops its execution."""
    excel_row = 2
    print("\n csv>>>>file>>>>>>>>", csv_file)

    # To count existing product's count
    product_count = models.execute_kw(
        db, uid, password, "product.template", "search_count", [[]]
    )
    print("product_count::::::::::::::", product_count)

    for row in csv_file:
        rec = dict(row)
        print("Rec -------------------", rec)
        if excel_row >= 2:
            # We used strip() method to remove white spaces from the record.
            product_tmpl_id = models.execute_kw(
                db,
                uid,
                password,
                "product.template",
                "search",
                [[["default_code", "=", rec["default_code"].strip()]]],
            )
            vals = {
                "name": rec["name"].strip(),
                "default_code": rec["default_code"].strip(),
                "list_price": rec["list_price"].strip(),
                "standard_price": rec["standard_price"].strip(),
            }
            if not product_tmpl_id:
                product_tmpl_id = models.execute_kw(
                    db, uid, password, "product.template", "create", [vals]
                )
            else:
                product_tmpl_id = models.execute_kw(
                    db,
                    uid,
                    password,
                    "product.template",
                    "write",
                    [[product_id[0]], vals],
                )
            print("\n\n:::::::::excel_row:::::::::::::::", excel_row)

            # Example of read method to fetch specific field like emails and name of partner
            # Read method default returns Id field.
            product_details = models.execute_kw(
                db,
                uid,
                password,
                "product.template",
                "read",
                [product_id],
                {"fields": ["name", "list_price"]},
            )
            print("product_details-------------", product_details)

        excel_row += 1

# Below print statements are used to get the start and end timings of the script execution.
print(":::::::::::::start::::::::::", start_time)
print("::::::End Time:::::::::", datetime.now())

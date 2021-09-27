import xmlrpc.client  # import to user xmlrpc API
import os
from datetime import datetime
import csv  # Imported to read csv files
url = 'http://127.0.0.1:9999'  # url:url of where odoo service is running
db = 'mydb'  # db: db which is defined in odoo service
username = 'admin'  # username : username through which we will login in db and make changes
password = 'admin'  # password: password of user name


common = xmlrpc.client.ServerProxy('%s/xmlrpc/2/common' % url)  # for authentication
version = common.version()  # to check if connection is correct before authentication
# Used as parameter while calling methods
uid = common.authenticate(db, username, password, {})
# Used as parameter while calling method
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

start_time = datetime.now()

with open('/home/odoo/workspace/odoo14c/odoo/custom_addons/shahil_xmlrpc_script/res.partner.csv', newline='') as csv_file:
    csv_file = csv.DictReader(csv_file)
    '''We use this variable for us while executing csv or excel file in xmlrc
    to know how many records are updated or inserted or if
    scripts stops its execution due to any reasons at that time we can get the
    row number of xls or csv file at which row script stops its execution.'''
    excel_row = 2
    print('\n csv>>>>file>>>>>>>>', csv_file)

    # To count existing product's count
    partner_count = models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[]])
    print("partner_count::::::::::::::", partner_count)

    for row in csv_file:
        rec = dict(row)
        print("Rec -------------------", rec)
        if excel_row >= 2:
            # We used strip() method to remove white spaces from the record.
            partner_id = models.execute_kw(db, uid, password, 'res.partner','search', [[['email', '=', rec['email'].strip()]]])
            print("\nPartner id --",partner_id)
            
            vals = {
                'name': rec['name'].strip(),
                'phone': rec['phone'].strip(),
                'email': rec['email'].strip(),
                'city': rec['city'].strip(),
                'country_id': country_id[0],
            }
            if not partner_id:
                partner_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [vals])
                print("\nPartner created--")
            else:
                partner_id = models.execute_kw(db, uid, password, 'res.partner', 'write',  [[partner_id[0]], vals])
                print("\nPartner update--")

            # if rec['city'] == 'Berlin':
            #     print("=Berlin=====")
            #     remove_partner_id = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['city', '=', 'Berlin']]])
            #     print("====remove partner==", remove_partner_id)
            #     models.execute_kw(db, uid, password, 'res.partner', 'unlink', [[partner for partner in remove_partner_id]])
            #     print(":::::::::remove::::::")

            print("\n\n:::::::::excel_row:::::::::::::::", excel_row)

            # Example of read method to fetch specific field like emails and name of partner
            # Read method default returns Id field.
            # partner_detials = models.execute_kw(db, uid, password, 'res.partner', 'read', [partner_id], {'fields': ['name','email']})
            # print("partner_details-------------", partner_detials)

        excel_row += 1

# Below print statements are used to get the start and end timings of the script execution.
print(":::::::::::::start::::::::::", start_time)
print("::::::End Time:::::::::", datetime.now())

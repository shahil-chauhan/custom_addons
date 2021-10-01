import xmlrpc.client
import os
from datetime import datetime
import csv

url = 'http://127.0.0.1:9999'
db = 'mydb'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy('%s/xmlrpc/2/common' % url)
version = common.version()
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

start_time = datetime.now()

with open('/home/odoo/workspace/odoo14c/odoo/custom_addons/shahil_xmlrpc_script/res.partner.csv', newline='') as csv_file:
    csv_file = csv.DictReader(csv_file)
    excel_row = 2
    print('\n csv>>>>file>>>>>>>>', csv_file)

    """count of partners"""
    partner_count = models.execute_kw(
        db, uid, password, 'res.partner', 'search_count', [[]])
    print("partner_count::::::::::::::", partner_count)

    for row in csv_file:
        rec = dict(row)
        if excel_row >= 2:
            partner_id = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['email', '=', rec['email'].strip()]]])
            print("\nPartner id --", partner_id)

                if rec['company_id'] == 'My Company (San Francisco)':
                    country_id = models.execute_kw(db, uid, password, 'res.country', 'search',[[['name', '=', rec['country_id']]]])
                
                    models.execute_kw(db, uid, password, 'res.partner', 'write', [[partner_id[0]],{'country_id': country_id[0]}])
                
                if rec['country_id'] == 'Berlin':
                    models.execute_kw(db, uid, password, 'res.partner', 'unlink',[[partner_id[0]]])

                vals = {
                    'name': rec['name'].strip(),
                    'phone': rec['phone'].strip(),
                    'email': rec['email'].strip(),
                    'city': rec['city'].strip(),
                }
                if not partner_id:
                    partner_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [vals])
                    print("\nPartner created--")
                else:
                    partner_id = models.execute_kw(db, uid, password, 'res.partner', 'write',  [[partner_id[0]], vals])
                    print("\nPartner update--")

            print("\n\n:::::::::excel_row:::::::::::::::", excel_row)

            excel_row += 1

print(":::::::::::::start::::::::::", start_time)
print("::::::End Time:::::::::", datetime.now())

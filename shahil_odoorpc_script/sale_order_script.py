import odoorpc
from datetime import datetime
import csv

odoo = odoorpc.ODOO('127.0.0.1', port=9999)
odoo.login('shahil_odoorpc_script', 'admin', 'admin')

start_time = datetime.now()

with open('/home/odoo/workspace/odoo14c/odoo/custom_addons/shahil_odoorpc_script/sale_order.csv',
          newline='') as csv_file:
    csv_file = csv.DictReader(csv_file)
    excel_row = 2
    for row in csv_file:
        rec = dict(row)
        print("\n\n read sale record ===================", rec)
        if excel_row >= 2:
            sale_order_id = odoo.env['sale.order'].search([('name', '=', rec['Order Reference'].strip())])
            print("===sale-order id====", sale_order_id)
            sale_order_id = odoo.env['sale.order'].browse(sale_order_id)
            print("======sale-order record-====", sale_order_id)

            partner_id = odoo.env['res.partner'].search([('name', '=', rec['Customer'])])
            print("===partner_id-====", partner_id)

            if not partner_id:
                print("===if not partner-===")
                partner = odoo.env['res.partner'].create({'name': rec['Customer']})
                partner_id.append(partner)
                print("====partner_id===", partner_id)

            sale_order_dict = {
                'name': rec['Order Reference'].strip(),
                'partner_id': partner_id[0],
                'amount_total': rec['Total'].strip(),
            }
            if not sale_order_id:
                print("====not sale order_id=======")
                sale_order_id = odoo.env['sale.order'].create([sale_order_dict])
            else:
                print("====else sale===")
                sale_order_id.write(sale_order_dict)

                print("\n\n:::::::::excel_row:sale order file::::::::::::::", excel_row)
        excel_row += 1

with open('/home/odoo/workspace/odoo14c/odoo/custom_addons/shahil_odoorpc_script/sale_order_line.csv',
          newline='') as csv_file:
    csv_file = csv.DictReader(csv_file)
    excel_row_line = 2
    for row in csv_file:
        rec = dict(row)
        print("\n\nRead order line record===================", rec)

        order_id = odoo.env['sale.order'].search([('name', '=', rec['Order Reference'].strip())])
        print("===order id-====", order_id)

        product_id = odoo.env['product.product'].search([('name', '=', rec['Description'].strip())])
        print("===product_id-====", product_id)

        if not product_id:
            print("===if not partner-===")
            product = odoo.env['product.product'].create({'name': rec['Description'].strip()})
            product_id.append(product)
            print("===after partner create===", product_id)

        sale_order_line_dict = {
            'order_id': order_id[0],
            'product_id': product_id[0],
            'name': rec['Description'].strip(),
            'product_uom_qty': rec['Quantity'].strip(),
            'price_subtotal': rec['Subtotal'].strip(),
            'price_unit': rec['Unit Price'].strip(),
            'product_uom': 1,
        }
        line_id = odoo.env['sale.order.line'].create([sale_order_line_dict])
        print("\n\n:::::::::excel_row_ order line file :::::::::::::::", excel_row_line)
    excel_row_line += 1

with open('/home/odoo/workspace/odoo14c/odoo/custom_addons/shahil_odoorpc_script/sale_order.csv',
          newline='') as csv_file:
    csv_file = csv.DictReader(csv_file)
    excel_row = 2
    for row in csv_file:
        rec = dict(row)
        print("\n\nRec sale file===================", rec)
        if excel_row >= 2:
            order_id = odoo.env['sale.order'].search([('name', '=', rec['Order Reference'].strip())])
            print("===order id-====", order_id)
            order_id = odoo.env['sale.order'].browse(order_id)
            print("===order id-=record===", order_id)

            if rec['Status'].strip() == 'Quotation':
                print("=====state in Quotation====")
                order_id.action_draft()
            if rec['Status'].strip() == 'Quotation Sent':
                print("=====state in sent====")
                order_id.action_quotation_sent()
            if rec['Status'].strip() == 'Sales Order':
                print("=====state in sale====")
                order_id.action_confirm()
            if rec['Status'].strip() == 'Locked':
                print("===== state in done====")
                order_id.state = 'done'
            if rec['Status'].strip() == 'Cancelled':
                print("=====state in cancel====")
                order_id.action_cancel()

# Below print statements are used to get the start and end timings of the script execution.
print(":::::::::::::start::::::::::", start_time)
print("::::::End Time:::::::::", datetime.now())

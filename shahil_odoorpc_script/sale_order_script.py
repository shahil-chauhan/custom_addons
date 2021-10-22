import csv
from datetime import datetime

import odoorpc

odoo = odoorpc.ODOO("127.0.0.1", port=9999)
odoo.login("shahil_odoorpc_db", "admin", "admin")

start_time = datetime.now()

with open(
    "/home/odoo/workspace/odoo14c/odoo/custom_addons/shahil_odoorpc_script/sale_order.csv",
    newline="",
) as csv_file:
    csv_file = csv.DictReader(csv_file)
    excel_row = 2
    for row in csv_file:
        rec = dict(row)
        if (
            excel_row >= 2
        ):  # To execute the file from the last row execute from the file
            print(":::::::::excel_row:sale order file::::::::::::", excel_row)
            print("\nSale Order Record=============\n", rec)
            sale_order_id = odoo.env["sale.order"].search(
                [("name", "=", rec["Order Reference"].strip())]
            )
            sale_order_id = odoo.env["sale.order"].browse(sale_order_id)
            partner_id = odoo.env["res.partner"].search(
                [("name", "=", rec["Customer"])]
            )

            if not partner_id:
                partner = odoo.env["res.partner"].create({"name": rec["Customer"]})
                partner_id.append(partner)
                print("====New Partner Created====", partner_id)

            sale_order_dict = {
                "name": rec["Order Reference"].strip(),
                "partner_id": partner_id[0],
                "amount_total": rec["Total"].strip(),
            }

            if not sale_order_id:
                print("====No sale order/Create New====")
                sale_order_id = odoo.env["sale.order"].create(sale_order_dict)
            else:
                print("====Update Sale Order===")
                sale_order_id.write(sale_order_dict)
        excel_row += 1

with open(
    "/home/odoo/workspace/odoo14c/odoo/custom_addons/shahil_odoorpc_script/sale_order_line.csv",
    newline="",
) as csv_file:
    csv_file = csv.DictReader(csv_file)
    excel_row = 2
    for row in csv_file:
        rec = dict(row)
        if (
            excel_row >= 2
        ):  # To execute the file from the last row execute from the file
            print("\n:::::::::excel_row::sale order line file::::::::::::", excel_row)
            print("\nSale Order line Record===========\n", rec)
            sale_order_id = odoo.env["sale.order"].search(
                [("name", "=", rec["Order Reference"].strip())]
            )
            product_id = odoo.env["product.product"].search(
                [("name", "=", rec["Description"].strip())]
            )

            if not product_id:
                product = odoo.env["product.product"].create(
                    {"name": rec["Description"].strip()}
                )
                product_id.append(product)
                print("===New Product Created===", product_id)

            sale_order_line_dict = {
                "order_id": sale_order_id[0],
                "product_id": product_id[0],
                "name": rec["Description"].strip(),
                "product_uom_qty": rec["Quantity"].strip(),
                "price_subtotal": rec["Subtotal"].strip(),
                "price_unit": rec["Unit Price"].strip(),
                "product_uom": 1,
            }
            print("====No order line/Create New====")
            sale_order_line_id = odoo.env["sale.order.line"].create(
                [sale_order_line_dict]
            )
        excel_row += 1

with open(
    "/home/odoo/workspace/odoo14c/odoo/custom_addons/shahil_odoorpc_script/sale_order.csv",
    newline="",
) as csv_file:
    csv_file = csv.DictReader(csv_file)
    excel_row = 2
    for row in csv_file:
        rec = dict(row)
        if (
            excel_row >= 2
        ):  # To execute the file from the last row execute from the file
            sale_order_id = odoo.env["sale.order"].search(
                [("name", "=", rec["Order Reference"].strip())]
            )
            sale_order_id = odoo.env["sale.order"].browse(sale_order_id)

            if rec["Status"].strip() == "Quotation":
                sale_order_id.action_draft()

            if rec["Status"].strip() == "Quotation Sent":
                sale_order_id.action_quotation_sent()

            if rec["Status"].strip() == "Sales Order":
                sale_order_id.action_confirm()

            if rec["Status"].strip() == "Locked":
                sale_order_id.state = "done"

            if rec["Status"].strip() == "Cancelled":
                sale_order_id.action_cancel()

# Below print statements are used to get the start and end timings of the script execution.
print(":::::::::::::start::::::::::", start_time)
print("::::::End Time:::::::::", datetime.now())

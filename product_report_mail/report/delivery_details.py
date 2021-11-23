from odoo import api, fields, models


class SaleDeliveryRecord(models.AbstractModel):
    _name = "report.sale.report_saleorder"
    _description = "Sale Delivery Record"

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env["sale.order"].browse(docids)
        print("\n\n\n\n\n Docids", docs)
        print("\n\n\n\n\n Docids", docids)
        delivery_orders_list = []
        for doc in docs:
            if doc.procurement_group_id:
                delivery_orders = self.env["stock.picking"].search(
                    [("group_id", "=", doc.procurement_group_id.id)]
                )
                delivery_orders_list.append(delivery_orders)
                print("\n\n\n\n\n\n\n Delivery order list", delivery_orders_list)

        return {
            "doc_ids": docs.ids,
            "doc_model": "sale.order",
            "docs": docs,
            "proforma": True,
            "delivery_orders_list": delivery_orders_list,
        }

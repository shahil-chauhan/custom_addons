import re
import urllib.parse as urlparse
from urllib.parse import parse_qs

from odoo import api, models


class DocumenterItem(models.Model):
    _inherit = "docu.item"

    @api.model
    def systray_get_help_items(self, url, version, app_name, channel):
        ordered_item_list, domain = [], []
        if channel:
            docu_version = self.env["docu.version"].search(
                [("name", "=", re.findall(r"\d+", version)[0])]
            )
            parsed = urlparse.urlparse(url)
            model = parse_qs(parsed.fragment).get("model")
            view_type = parse_qs(parsed.fragment).get("view_type")
            domain = []
            if docu_version:
                domain += [
                    "|",
                    ("version_id", "=", False),
                    ("version_id", "=", docu_version.id),
                ]
            if channel in ["all", "general"]:
                items = self.search(domain)
            elif channel == "forus":
                items = self.search(
                    domain + [("partner_id", "=", self.env.user.partner_id.id)]
                )
            if app_name and model:
                app = self.env["ir.module.module"].search(
                    [("shortdesc", "=", app_name)]
                )
                if len(app) > 1:
                    app = app.filtered(lambda l: l.application)
                ir_model = self.env["ir.model"].search([("model", "in", model)])
                filtered_item_ids = items.filtered(
                    lambda l: (app.id in l.apps.mapped("id"))
                    and (view_type and view_type[0] in l.views.mapped("view_type"))
                    and ir_model.id in l.models.ids
                    and l.partner_id.id == self.env.user.partner_id.id
                ).ids
                ordered_item_list = [
                    item
                    for item in self.search(
                        [("id", "in", filtered_item_ids)], order="write_date desc"
                    )
                ]
                filtered_item_ids = items.filtered(
                    lambda l: (app.id in l.apps.mapped("id"))
                    and (view_type and view_type[0] in l.views.mapped("view_type"))
                    and ir_model.id in l.models.ids
                    and (
                        not l.partner_id
                        or l.partner_id.id != self.env.user.partner_id.id
                    )
                ).ids
                ordered_item_list += [
                    item
                    for item in self.search(
                        [("id", "in", filtered_item_ids)], order="write_date desc"
                    )
                ]
                filtered_item_ids = items.filtered(
                    lambda l: (app.id in l.apps.mapped("id"))
                    and (
                        not view_type
                        or (
                            view_type
                            and view_type[0] not in l.views.mapped("view_type")
                        )
                    )
                    and ir_model.id in l.models.ids
                    and l.partner_id.id == self.env.user.partner_id.id
                ).ids
                ordered_item_list += [
                    item
                    for item in self.search(
                        [("id", "in", filtered_item_ids)], order="write_date desc"
                    )
                ]
                filtered_item_ids = items.filtered(
                    lambda l: (app.id in l.apps.mapped("id"))
                    and (
                        not view_type
                        or (
                            view_type
                            and view_type[0] not in l.views.mapped("view_type")
                        )
                    )
                    and ir_model.id in l.models.ids
                    and (
                        not l.partner_id
                        or l.partner_id.id != self.env.user.partner_id.id
                    )
                ).ids
                ordered_item_list += [
                    item
                    for item in self.search(
                        [("id", "in", filtered_item_ids)], order="write_date desc"
                    )
                ]
                filtered_item_ids = items.filtered(
                    lambda l: (app.id in l.apps.mapped("id"))
                    and (view_type and view_type[0] in l.views.mapped("view_type"))
                    and ir_model.id not in l.models.ids
                    and l.partner_id.id == self.env.user.partner_id.id
                ).ids
                ordered_item_list += [
                    item
                    for item in self.search(
                        [("id", "in", filtered_item_ids)], order="write_date desc"
                    )
                ]
                filtered_item_ids = items.filtered(
                    lambda l: (app.id in l.apps.mapped("id"))
                    and (
                        not view_type
                        or (
                            view_type
                            and view_type[0] not in l.views.mapped("view_type")
                        )
                    )
                    and ir_model.id not in l.models.ids
                    and l.partner_id.id == self.env.user.partner_id.id
                ).ids
                ordered_item_list += [
                    item
                    for item in self.search(
                        [("id", "in", filtered_item_ids)], order="write_date desc"
                    )
                ]
                filtered_item_ids = items.filtered(
                    lambda l: (app.id in l.apps.mapped("id"))
                    and (
                        not view_type
                        or (
                            view_type
                            and view_type[0] not in l.views.mapped("view_type")
                        )
                    )
                    and ir_model.id not in l.models.ids
                    and (
                        not l.partner_id
                        or l.partner_id.id != self.env.user.partner_id.id
                    )
                ).ids
                ordered_item_list += [
                    item
                    for item in self.search(
                        [("id", "in", filtered_item_ids)], order="write_date desc"
                    )
                ]
            else:
                if channel in ["all", "general"]:
                    ordered_item_list += [
                        item for item in self.search(domain, order="write_date desc")
                    ]
                elif channel == "forus":
                    ordered_item_list += [
                        item
                        for item in self.search(
                            domain + [("partner_id", "=", self.env.user.partner_id.id)],
                            order="write_date desc",
                        )
                    ]
            if channel == "general":
                return (
                    self.search_read(
                        domain
                        + [("id", "not in", [item.id for item in ordered_item_list])],
                        ["name", "description_short", "item_type"],
                    )[:10],
                    self.search_count([]),
                )
            return [
                {
                    "id": item.id,
                    "name": item.name,
                    "description_short": item.description_short,
                    "item_type": item.item_type,
                }
                for item in ordered_item_list
            ][:10], self.search_count([])

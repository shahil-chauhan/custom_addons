import random
import string
from odoo import api, fields, models
from odoo.tools.translate import _


class Product(models.Model):
    _inherit = "product.template"

    random_string = fields.Char(
        string=_("Random String"),
        compute="_compute_random_string",
        inverse="_set_random_string",
    )

    @api.depends("product_variant_ids", "product_variant_ids.random_string")
    def _compute_random_string(self):
        print("\n\n\n\n\n _compute_random_string\n\n\n self before loop: ", self)

        unique_variants = self.filtered(lambda temp: len(temp.product_variant_ids) == 1)
        print("\n\n\n\n\n unique_variants: ", unique_variants)

        for temp in unique_variants:
            print("\n\n\n\n\n temp inside loop:[]", temp)
            temp.random_string = temp.product_variant_ids.random_string
            print(
                "\n\n\n\n\n temp.product_variant_ids.random_string:[] and temp.random_string:[] ",
                temp.product_variant_ids.random_string,
                temp.random_string,
            )

    def _set_random_string(self):
        print("\n\n\n\n\n _set_random_string\n\n\n self before loop: ", self)
        for temp in self:
            print("\n\n\n\n\n self inside loop:[]: [] ", self, temp)

            if len(temp.product_variant_ids) == 1:
                print(
                    "\n\n\n\n\n temp.product_variant_ids inside if:[] and len:[] ",
                    temp.product_variant_ids,
                    len(temp.product_variant_ids),
                )

                temp.product_variant_ids.random_string = temp.random_string
                print(
                    "\n\n\n\n\n temp.product_variant_ids.random_string inside if:[] and temp.random_string:[] ",
                    temp.product_variant_ids.random_string,
                    temp.random_string,
                )

    def random_string_generate(self):
        print("\n\n\n\n\n generate_random_string 1.0\n\n\n", self)

        str = "".join(
            random.choices(
                string.ascii_uppercase + string.digits + string.ascii_lowercase, k=5
            )
        )
        self.update({"random_string": str})


class Productvatiant(models.Model):
    _inherit = "product.product"

    random_string = fields.Char(readonly=True, string=_("Random String"))

    def random_string_generate(self):
        print("\n\n\n\n\n generate_random_string 1.1\n\n\n", self)

        str = "".join(
            random.choices(
                string.ascii_uppercase + string.digits + string.ascii_lowercase, k=5
            )
        )
        self.update({"random_string": str})

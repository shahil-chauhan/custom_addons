from odoo import http
from odoo.http import request, route


class ProductList(http.Controller):
    @http.route("/product", type="http", website=True, auth="public")
    def product_page(self):
        product = request.env['product.template'].sudo().search([])
        return request.render("product_website.product_website_template", {"product": product})


class Product(http.Controller):
    @http.route("/product/<model('product.template'):product>", type="http", website=True, auth="public")
    
    def product_item_page(self, product, **kw):
        return request.render("product_website.product_item_template", {"product_item": product})

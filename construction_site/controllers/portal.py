from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager
from odoo.http import request, route
from odoo import http



class CustomerPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        values['sites_count'] = request.env['construction.site'].search_count([])
        return values


    @http.route(['/my/construction_site', '/my/construction_site/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_sites(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        sites = request.env['construction.site'].search([])
        return request.render("construction_site.portal_my_construction", {'sites': sites})

from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager
from odoo.http import request, route
from odoo import http, _
from collections import OrderedDict


class CustomerPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        values['sites_count'] = request.env['construction.site'].search_count([
        ])
        return values

    @http.route(['/my/construction_site', '/my/construction_site/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_sites(self, page=1, sortby=None, filterby=None, **kw):
        values = self._prepare_portal_layout_values()
        ConstructionSite = request.env['construction.site']

        domain=[]
        searchbar_sortings = {
            'date': {'label': _('Date'), 'order': 'schedule_date desc'},
            'name': {'label': _('Name'), 'order': 'name'},
        }

        # # default sortby order
        if not sortby:
            sortby = 'name'
        sort_order = searchbar_sortings[sortby]['order']

        searchbar_filters = {
            'all': {'label': 'All', 'domain': []},
            'draft': {'label': 'Draft', 'domain': [('state', '=', 'draft')]},
        }
        # default filter by value
        if not filterby:
            filterby = 'all'
        domain += searchbar_filters[filterby]['domain']

        # count for pager
        sites_count = ConstructionSite.search_count(domain)
        
        # make pager
        pager = portal_pager(
            url="/my/construction_site",
            url_args={'sortby': sortby,'filterby': filterby},
            total=sites_count,
            page=page,
            step=self._items_per_page
        )
        
        # search the count to display, according to the pager data
        sites = ConstructionSite.search(
            domain, order=sort_order, limit=self._items_per_page, offset=pager['offset'])
        request.session['my_construction_history'] = sites.ids[:100]

        values.update({
            'sites': sites,
            'page_name': 'site',
            'pager': pager,
            'default_url': '/my/construction_site',
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
            'searchbar_filters': OrderedDict(sorted(searchbar_filters.items())),
            'filterby': filterby,
        })
        return request.render("construction_site.portal_my_construction", values)

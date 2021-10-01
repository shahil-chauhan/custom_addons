odoo.define('systray.HelpMenu', function (require) {
"use strict";

var core = require('web.core');
var session = require('web.session');
var SystrayMenu = require('web.SystrayMenu');
var Widget = require('web.Widget');
var FormController = require('web.FormController');
var FormRenderer = require('web.FormRenderer');
var FormView = require('web.FormView')

var QWeb = core.qweb;
var _t = core._t;

FormController.include({
    init: function (parent, model, renderer, params) {
        this._super.apply(this, arguments);
        var context = params.initialState.context;
        if (_.has(context, "preview_doc_item_readonly")){
            params.activeActions.create = false;
            params.activeActions.edit = false;
        }
    },
});

FormRenderer.include({
    _applyModifiers: function (modifiersData, record, element) {
        var self = this;
        this._super.apply(this, arguments);
        if (element) {
            var node = self.state.data[modifiersData.node.attrs.name];
            var context = self.state.context;
            if ((_.has(context, "preview_doc_item_readonly")) && (node == false || node == "" || node == "<p><br></p>" || (typeof(node) === 'object' && node.count == 0))){
                element.$el.addClass("o_invisible_modifier");
            }
        }
    },
});

FormView.include({
    _extractParamsFromAction: function (action) {
        var params = this._super.apply(this, arguments);
        if (_.has(action.context, "preview_doc_item_readonly")){
            params.mode = 'readonly';
        }
        return params;
    },
});

var HelpMenu = Widget.extend({
    name: 'help_menu',
    template:'help_icon.HelpMenu',
    events: {
        'show.bs.dropdown': '_onItemMenuShow',
        'click .o_see_all_items': '_onClickSeeAllButton',
        'click .docu_item_preview': '_onClickItemPreview',
        'click li.all': '_viewChannelInfo',
        'click li.forus': '_viewChannelInfo',
        'click li.general': '_viewChannelInfo',
    },
    start: function () {
        this._$itemsPreview = this.$('.o_help_dropdown_items');
        this._updateHelpPreview();
        return this._super();
    },

    _updateHelpPreview: function (app) {
        var self = this;
        self.activeTabId = "all";
        self.app = app;
        return this._rpc({
            model: 'docu.item',
            method: 'systray_get_help_items',
            args: [window.location.href, session.server_version, app, 'all'],
        }).then(function (data) {
            self._items = data[0];
            self._$itemsPreview.html(QWeb.render('help_icon.systray.HelpMenu.Previews', {
                widget: self,
                total_items: data[1],
            }));
        });
    },

    _onItemMenuShow: function (ev) {
        if(this.activeTabId != "all"){
            ev.preventDefault();
        }
        document.body.classList.add('modal-open');
        var app = $(ev.currentTarget).parents('ul.o_menu_systray').prev('ul.o_menu_sections').prev('a.o_menu_brand')[0].innerText;
        this._updateHelpPreview(app);
    },

    _onClickSeeAllButton: function() {
        var self = this;
        self.do_action({
            type: 'ir.actions.act_window',
            res_model: 'docu.item',
            views: [[false, 'list'],[false, 'form']],
            target: 'current',
            domain: self.help_domain,
            name: 'Items'
        });
    },

    _viewChannelInfo: function(ev) {
        ev.preventDefault();
        var self = this;
        return this._rpc({
            model: 'docu.item',
            method: 'systray_get_help_items',
            args: [window.location.href, session.server_version, self.app, ev.currentTarget.dataset.id],
        }).then(function (data) {
            self._items = data[0];
            self.activeTabId = ev.currentTarget.dataset.id;
            self._$itemsPreview.html(QWeb.render('help_icon.systray.HelpMenu.Previews', {
                widget: self,
                total_items: data[1],
            }));
            self.$el.addClass('show');
        });
    },

    _onClickItemPreview: function(event) {
        var itemId = parseInt($(event.target).attr('data-id'));
        this.do_action({
            type: 'ir.actions.act_window',
            res_model: 'docu.item',
            res_id: itemId,
            views: [[false, 'form']],
            target: 'new',
            context: {'preview_doc_item_readonly': true},
        });
    },

});

SystrayMenu.Items.push(HelpMenu);

return HelpMenu;

});

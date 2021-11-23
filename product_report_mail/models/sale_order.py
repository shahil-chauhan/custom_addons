from odoo import _, api, fields, models
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    partner_cust_ids = fields.Many2many(
        "res.partner", "partner_rel", "sa_id", "par_id", string="Partner"
    )

    def mail_wizard_button(self):
        print("\n\n\n\n update M2M calling.... \n\n\n\n")
        # self.partner_cust_ids= [(6,0,[14,23,33])]
        # self.partner_cust_ids = [(4,27)]
        # self.partner_cust_ids = [(5,)]
        # [0,0,{}]
        # range_list=[]
        # for i in range(0,2):
        #     cust_dict={'name':i}
        #     range_list.append(cust_dict)
        # for val in range_list:
        #     print ("iiiiiiiiii",val)
        #     self.partner_cust_ids = [(0,0,val)]

        # self.partner_cust_ids= [(2,44)] - Delete
        # self.partner_cust_ids= [(1,43,{'phone':'8460232337'})]

        # self.ensure_one()
        # template_id = self._find_mail_template()
        # # template_custom_id = self.env.ref('module_name.template_id')
        # lang = self.env.context.get('lang')
        # template = self.env['mail.template'].browse(template_id)
        # if template.lang:
        #     lang = template._render_lang(self.ids)[self.id]
        # ctx = {
        #     'default_model': 'sale.order',
        #     'default_res_id': self.ids[0],
        #     'default_partner_ids':[(6,0,[14,23,33])],
        #     'default_use_template': bool(template_id),
        #     'default_template_id': template_id,
        #     'default_composition_mode': 'comment',
        #     'mark_so_as_sent': True,
        #     'custom_layout': "mail.mail_notification_paynow",
        #     'proforma': self.env.context.get('proforma', False),
        #     'force_email': True,
        #     'model_description': self.with_context(lang=lang).type_name,
        # }
        # ctx= {
        #     'default_phone':'84555555532',
        #     'my_name':'arti'
        # }
        # return {
        #     'type': 'ir.actions.act_window',
        #     'view_mode': 'form',
        #     'res_model': 'res.partner',
        #     'views': [(False, 'form')],
        #     'view_id': False,
        #     'target': 'new',
        #     'context': ctx,
        # }

    # User Define constraint
    # def action_confirm(self):
    #     result = super(SaleOrder, self).action_confirm()
    #     print("Productsss in order line")
    #     if not self.order_line:
    #         print("No productss")
    #         raise UserError(_('Pls select product'))
    #     return result

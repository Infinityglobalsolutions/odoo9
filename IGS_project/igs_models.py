'''
Created on Sep 26, 2016

@author: user
'''
from openerp import  fields, models

class igs_sale_order(models.Model):
    _name = "sale.order"
    _inherit = "sale.order"

    date_order = fields.Datetime(string='Order Date', required=True, readonly=True, index=True, states={'draft': [('readonly', False)],'sale': [('readonly', False)], 'sent': [('readonly', False)]}, copy=False, default=fields.Datetime.now)
    
class igs_accountInvoice(models.Model):
    _name = "account.invoice"
    _inherit ="account.invoice"
    
    date_invoice = fields.Date(string='Invoice Date',
        readonly=True, states={'draft': [('readonly', False)], 'open':[('readonly',False)]}, index=True,
        help="Keep empty to use the current date", copy=False)
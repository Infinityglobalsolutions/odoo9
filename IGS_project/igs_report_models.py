'''
Created on Oct 3, 2016

@author: user
'''
from openerp import models, fields, api, _

class report_payment(models.AbstractModel):
    _name = 'report.igs_report_models.report_payment'
    _template = 'igs_report_models.report_payment'
    def get_format(self):
        return 'some text!!!'
    @api.multi
    def render_html(self, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name(self._template)
        docargs = {
            'get_format': self.get_format,
            'doc_ids': self._ids,
            'doc_model': report.model,
            'docs': self,
        }
        return report_obj.render(self._template, docargs)
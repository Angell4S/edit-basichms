from odoo import models, fields, api, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    _description = _('Sale Order Line')

    patient_id = fields.Many2one(
        string=_('Paciente'),
        comodel_name='medical.patient',
        compute='_compute_patient_id',
    )

    @api.depends('order_id')
    def _compute_patient_id(self):
        patient_model = self.env['medical.patient']
        for record in self:
            record.patient_id = patient_model.search(
                [('patient_id', '=', record.order_id.partner_id.id)]
            ).id

    def _prepare_invoice_line(self, **optional_values):
        res = super(SaleOrderLine, self)._prepare_invoice_line()
        res.update(
            {
                'patient_id': self.patient_id.id,
            }
        )
        return res

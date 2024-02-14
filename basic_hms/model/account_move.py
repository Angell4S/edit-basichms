from odoo import models, fields, api, _


class AccountMove(models.Model):
    _inherit = 'account.move'
    _description = _('Account Move')

    def create_history_lines(self):
        vals = []
        for l in self.line_ids:
            if l.product_id.id:
                vals.append(
                    {
                        'move_line_id': l.id,
                        'patient_id': l.patient_id.id,
                    }
                )
        self.env['medical.patient.history'].create(vals)

    def action_post(self):
        self.create_history_lines()
        return super(AccountMove, self).action_post()


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    _description = _('Account Move Line')

    patient_id = fields.Many2one(
        string=_('Patient'),
        comodel_name='medical.patient',
    )
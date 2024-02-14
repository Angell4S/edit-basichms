from odoo import models, fields, api, _


class MedicalPatientHistory(models.Model):
    _name = 'medical.patient.history'
    _description = _('Medical Patient History')

    name = fields.Char(string=_('Name'))

    move_line_id = fields.Many2one(
        string=_('Sevice'),
        comodel_name='account.move.line',
    )
    product_id = fields.Char(
        related='move_line_id.product_id.name',
        string=_('Treatment'),
    )
    move_id = fields.Many2one(
        related='move_line_id.move_id',
        comodel_name='account.move',
        string=_('Move'),
    )
    treatment_date = fields.Date(
        related='move_id.date',
        string=_('Treatment Date'),
    )

    before_image_ids = fields.One2many(
        string=_('Images'),
        comodel_name='multi.image',
        inverse_name='history_id',
    )
    before_image = fields.Binary(string=_('Images'))
    after_image_ids = fields.One2many(
        string=_('After Images'),
        comodel_name='multi.image',
        inverse_name='history_id',
    )
    after_image = fields.Binary(string=_('After Image'))

    patient_id = fields.Many2one(
        string=_('Patient'),
        comodel_name='medical.patient',
    )

    observation = fields.Text(string=_('Observation'))

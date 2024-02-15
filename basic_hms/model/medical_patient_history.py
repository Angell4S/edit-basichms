from odoo import models, fields, api, _


class MedicalPatientHistory(models.Model):
    _name = 'medical.patient.history'
    _description = _('Medical Patient History')

    name = fields.Char(string=_('Nombre'))

    move_line_id = fields.Many2one(
        string=_('Servicio'),
        comodel_name='account.move.line',
    )
    product_id = fields.Char(
        related='move_line_id.product_id.name',
        string=_('Tratamiento'),
    )
    move_id = fields.Many2one(
        related='move_line_id.move_id',
        comodel_name='account.move',
        string=_('Factura'),
    )
    treatment_date = fields.Date(
        related='move_id.date',
        string=_('Fecha de la Factura'),
    )

    before_image_ids = fields.One2many(
        string=_('Imágenes'),
        comodel_name='multi.image',
        inverse_name='history_id',
    )
    before_image = fields.Binary(string=_('Imágenes'))
    after_image_ids = fields.One2many(
        string=_('After Images'),
        comodel_name='multi.image',
        inverse_name='history_id',
    )
    after_image = fields.Binary(string=_('After Image'))

    patient_id = fields.Many2one(
        string=_('Paciente'),
        comodel_name='medical.patient',
    )

    control_date = fields.Date(string=_('Fecha del Control'))

    observation = fields.Text(string=_('Observaciones'))

    obs_state = fields.Selection(
        string=_('Estado de las Observaciones'),
        selection=[
            ('with_obs', 'Con Observaciones'),
            ('without_obs', 'Sin Observaciones'),
        ],
        compute='_compute_obs_state',
        default='without_obs',
        store=True,
    )

    @api.depends('observation')
    def _compute_obs_state(self):
        if isinstance(self.observation, str) or self.observation != '':
            self.obs_state = 'with_obs'

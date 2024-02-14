# -*- coding: utf-8 -*-
import logging

import base64

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError

from odoo.addons.web_editor.tools import (
    get_video_embed_code,
    get_video_thumbnail,
)

_logger = logging.getLogger(__name__)


class MultiImage(models.Model):
    _name = 'multi.image'
    _description = _('MultiImage')
    _inherit = ['image.mixin']
    _order = 'sequence, id'

    name = fields.Char(_('Name'))
    sequence = fields.Integer(default=10)

    image_1920 = fields.Image()

    history_id = fields.Many2one(
        string=_('History'),
        comodel_name='medical.patient.history',
    )
    upload_date = fields.Date(
        string=_('Upload_date'),
        default=fields.Date.context_today,
    )

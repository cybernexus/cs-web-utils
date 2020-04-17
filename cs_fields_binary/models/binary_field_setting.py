# -*- coding: utf-8 -*-

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

class BinaryFieldOption(models.Model):
    _name = 'binary.field.setting'
    _description = 'Extra Settings / Overides for binary fields'
    _rec_name = 'ir_model_field_id'

    ir_model_field_id = fields.Many2one('ir.model.fields', string='Field', domain=[('ttype','=','binary')])

    accepted_file_override = fields.Char(string='Accepted File Override', help='Comma delimited list (ex. .jpg,.png')

    file_size_mb = fields.Integer(string='File Upload Size Override')

    @api.model
    def get_settings(self, model, field):
        binary_field_setting = self.env['binary.field.setting'].search(['&',('ir_model_field_id.model','=', model),('ir_model_field_id.name','=', field)],limit=1)
        settings = { 'accepted_file_override': '', 'file_size_mb': 0 }
        if binary_field_setting:
            settings['accepted_file_override'] = binary_field_setting.accepted_file_override
            settings['file_size_mb'] = binary_field_setting.file_size_mb
        
        return settings


    
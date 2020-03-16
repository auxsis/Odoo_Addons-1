# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    has_facebook_pixel = fields.Boolean(related='website_id.has_facebook_pixel')
    facebook_pixel_key = fields.Char(related='website_id.facebook_pixel_key')

    @api.onchange('has_facebook_pixel')
    def onchange_has_facebook_pixel(self):
        if not self.has_facebook_pixel:
            self.facebook_pixel_key = False

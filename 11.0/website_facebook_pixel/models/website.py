# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Website(models.Model):
    _inherit = 'website'

    has_facebook_pixel = fields.Boolean('Facebook Pixel')
    facebook_pixel_key = fields.Char('Facebook Pixel ID')

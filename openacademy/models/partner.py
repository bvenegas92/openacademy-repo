# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'
    _description = "Model to store partner"

    instructor = fields.Boolean(default=False)
    session_ids = fields.Many2many('openacademy.session', string="Attended Sessions", readonly=True)
    other_field = fields.Boolean(default=False)
    other_field2 = fields.Boolean(default=False)
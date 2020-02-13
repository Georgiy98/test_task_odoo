# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class Product(models.Model):
    _name = "test.product"

    name = fields.Char()

    #currency_id = fields.Many2one('res.currency',default=lambda self: self.env.user.company_id.currency_id.id)
    #cost = fields.Monetary(currency_field='currency_id')
    cost = fields.Float(digits=(10,2))
    subcategory_id = fields.Many2one("test.subcategory")
    group_ids = fields.Many2many("test.group")
    #team_id = fields.Many2one("job.team")

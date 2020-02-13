# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class Subcategory(models.Model):
    _name = "test.subcategory"
    name = fields.Char()
    category_id = fields.Many2one("test.category")
    product_ids = fields.One2many("test.product","subcategory_id")
    group_ids = fields.One2many("test.group","subcategory_id")

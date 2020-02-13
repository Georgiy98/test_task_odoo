# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class Category(models.Model):
    _name = "test.category"
    name = fields.Char()
    subcategory_ids = fields.One2many("test.subcategory","category_id")
    group_ids = fields.One2many("test.group","category_id")

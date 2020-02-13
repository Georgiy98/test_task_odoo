# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class Group(models.Model):
    _name = "test.group"

    @api.onchange("product_ids")
    def get_cost(self):
        for obj in self:
            res = 0
            for product in obj.product_ids:
                res+=product.cost
            obj.cost = res
    name = fields.Char()
    created_date = fields.Date(default = fields.Date.today(),readonly = True)

    category_id = fields.Many2one("test.category")
    subcategory_id = fields.Many2one("test.subcategory")
    product_ids = fields.Many2many("test.product")

    currency_id = fields.Many2one('res.currency',default=lambda self: self.env.user.company_id.currency_id.id)
    cost = fields.Monetary(compute = "get_cost",default = 0,currency_field='currency_id')

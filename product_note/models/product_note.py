# -*- coding: utf-8 -*-

from odoo import models, fields

class ProductNote(models.Model):
    _name = 'product.note'
    _description = 'Product Notes'

    name = fields.Char(string='Note Title', required=True)
    product_id = fields.Many2one(
        'product.product', 
        string='Product', 
        required=True
    )
    note = fields.Text(string='Note')
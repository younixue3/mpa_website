from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    favorite_product_ids = fields.Many2many('product.template', string="Favorite Products")

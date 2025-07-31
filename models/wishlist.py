from odoo import models, fields, api

class Wishlist(models.Model):
    _name = 'product.wishlist'
    _description = 'Product Wishlist'
    _sql_constraints = [
        ('unique_user_product', 'unique(user_id, product_id)', 'You have already added this product to your wishlist!')
    ]

    user_id = fields.Many2one('res.users', string='User', required=True, default=lambda self: self.env.user)
    product_id = fields.Many2one('product.template', string='Product', required=True)

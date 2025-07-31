from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    favorite_product_ids = fields.Many2many(
        'product.template',  # Model yang di-relasikan
        'res_partner_favorite_product_rel',  # Nama tabel relasi
        'partner_id',  # Kolom ID partner
        'product_id',  # Kolom ID produk
        string="Favorite Products"
    )

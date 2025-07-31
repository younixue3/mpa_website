from odoo import http
from odoo.http import request

class HomePageController(http.Controller):

    @http.route('/home_page', type='http', auth='public', website=True)
    def home_page(self, **kwargs):
        # Render the form page template
        return request.render('mpa_website.home_page')

    @http.route('/about', type='http', auth='public', website=True)
    def about_page(self, **kwargs):
        # Render the form page template
        return request.render('mpa_website.about_page')

    @http.route('/product', type='http', auth='public', website=True)
    def product_page(self, **kwargs):
        # Render the form page template
        return request.render('mpa_website.product_page')

    @http.route('/iup', type='http', auth='public', website=True)
    def iup_page(self, **kwargs):
        # Render the form page template
        return request.render('mpa_website.iup_page')

    @http.route('/proyek', type='http', auth='public', website=True)
    def proyek_page(self, **kwargs):
        # Render the form page template
        return request.render('mpa_website.proyek_page')
    
    @http.route('/blog', type='http', auth='public', website=True)
    def blog_page(self, **kwargs):
        # Render the form page template
        return request.render('mpa_website.blog_page')
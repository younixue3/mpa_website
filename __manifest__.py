{
    'name': 'MPA Website',
    'version': '1.0',
    'summary': 'MPA Web Page',
    'description': 'Web Design Development',
    'category': 'Website',
    'author': '-',
    'depends': ['website', 'sale', 'contacts', 'portal', 'website_blog'],
    'data': [
        'views/layout/footer.xml',
        'views/layout/header.xml',
        'views/assets.xml',
        # home
        'views/page/home/index.xml',
        'views/page/home/components/heroSection.xml',
        'views/page/home/components/aboutSection.xml',
        'views/page/home/components/videoSection.xml',
        'views/page/home/components/productSection.xml',
        'views/page/home/components/sandSection.xml',
        'views/page/home/components/guaranteeSection.xml',
        'views/page/home/components/serviceSection.xml',
        'views/page/home/components/mapSection.xml',
        # about
        'views/page/about/index.xml',
        'views/page/about/components/heroSection.xml',
        'views/page/about/components/aboutSection.xml',
        'views/page/about/components/visiMisiSection.xml',
        'views/page/about/components/valueSection.xml',
        'views/page/about/components/mapSection.xml',
        'views/page/about/components/proyekSection.xml',
        'views/page/about/components/fasilitySection.xml',
        'views/page/about/components/legalSection.xml',
        'views/page/about/components/guaranteeSection.xml',
        # product
        'views/page/product/index.xml',
        'views/page/product/components/heroSection.xml',
        'views/page/product/components/videoSection.xml',
        'views/page/product/components/proyekSection.xml',
        'views/page/product/components/materialSection.xml',
        'views/page/product/components/materialDesktopSection.xml',
        'views/page/product/components/videoSection.xml',
        'views/page/product/components/videoMobileSection.xml',
        # iup
        'views/page/iup/index.xml',
        'views/page/iup/components/heroSection.xml',
        'views/page/iup/components/aboutSection.xml',
        'views/page/iup/components/iupSection.xml',
        # proyek
        'views/page/proyek/index.xml',
        'views/page/proyek/components/heroSection.xml',
        'views/page/proyek/components/clientSection.xml',
        # blog
        'views/page/blog/index.xml',
        'views/page/blog/components/heroSection.xml',
        'views/page/blog/components/blogSection.xml',
        

    ],
    'qweb': [],  # Jika ada QWeb template tambahan, masukkan di sini
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

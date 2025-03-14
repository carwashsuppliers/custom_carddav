{
    'name': 'CardDAV Server for Contacts',
    'version': '1.0',
    'summary': 'Expose Odoo contacts via CardDAV',
    'category': 'Tools',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'depends': ['contacts', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'views/carddav_settings.xml',
        'data/carddav_demo.xml',
    ],
    'installable': True,
    'application': True,
}

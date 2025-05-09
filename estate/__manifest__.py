{
    'name': 'Estate',
    'version': '1.0',
    'summary': 'Gestió de propietats immobiliàries',
    'category': 'Real Estate',
    'license': 'LGPL-3',
    'author': 'El teu nom',
    'depends': ['base'],
    'application': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_reports_views.xml',
        'views/estate_menus.xml',
        'views/estate_property_view_filter.xml',
        'report/estate_property_reports.xml',
        'report/estate_property_templates.xml',
    ],
}
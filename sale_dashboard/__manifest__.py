# -*- coding: utf-8 -*-
{
    'name': "sale_dashboard",
    'summary': """This module will add dashboard in sale module""",
    'description': """This module will add dashboard in sale module which
                    shows the last month sale report""",
    'author': "Aktiv software",
    'website': "http://www.aktivsoftware.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'sale_management', 'board'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/dashboard_view.xml',
        'views/assets.xml',
    ],
    'qweb': [
        'static/src/xml/templates.xml'
    ]
}

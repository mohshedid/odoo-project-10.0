# -*- coding: utf-8 -*-
{
    'name': "auth_oauth_weixin",

    'summary': """
        for weixin authorization and login into Odoo 
        """,

    'description': """

    """,

    'author': 'Gavin GU',
    'category': 'Tools',
    'version': '0.1',

    'depends': ['auth_oauth'],

    'data': [
        'security/ir.model.access.csv',
        'auth_oauth_data.xml',
    ],

    'installable': True,

}

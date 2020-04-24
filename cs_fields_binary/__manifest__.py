# -*- coding: utf-8 -*-
{
    'name': "CS Web Utils",
    'summary': "CS Web Utility module",
    'description':
    """
        This module provides these additional fields options:
        - accept on binaryfile field
        - upload file size overrides on binaryfile field.
    """,
    'author': "Cybernexus Solutions",
    'category': "Web",
    "license": "AGPL-3",
    'version': "13.0.1.0.0",
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base','web'],
    'data': [
        'templates/web_base.xml',
    ],
    'qweb': ['static/src/xml/widget_binaryfile.xml']
}

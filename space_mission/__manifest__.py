# -*- coding: utf-8 -*-
{
    'name': "Space Mission (MT)",
    'summary': """
        Space mission for ODoo training (MT)""",
    'description': """
        Application to organize the logistics including spaceship and space crew
    """,
    'author': "Mehdi Tepava",
    'images' : ['static/src/description/icon.png'],
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['approvals','contacts','project'],
    'data': [
        'security/space_mission_security.xml',
        'security/ir.model.access.csv',
        'views/space_mission_menuitems.xml',
        'views/ship_view.xml',
        'views/library_view.xml',
        'views/cooperative_view.xml',
        'views/mission_view.xml',
        'views/rental.xml',
        'views/project_views_inherit.xml',
        'views/book_copy.xml',
        'views/approval_views_inherit.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/module_demo.xml'
    ],
    
    'license': 'LGPL-3',
    'application': True,
}
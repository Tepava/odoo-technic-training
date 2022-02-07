# -*- coding: utf-8 -*-
{
    'name': "Space Mission (MT)",
    'summary': """
        Space mission for ODoo training (MT)""",
    'description': """
        Application to organize the logistics including spaceship and space crew
    """,
    'author': "Mehdi Tepava",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','space_mission_library_management','space_mission_shop_volunteer'],
    'data': [
        #'security/ir.model.access.csv',
        #'views/settings.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    'license': 'LGPL-3',
}
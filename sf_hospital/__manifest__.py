# -*- coding: utf-8 -*-
# Custom module from Peter Gichia, free for use, LICENCE under MIT.


{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'Peter Gichia',
    'summary': 'Manage hospital appointments',
    'description': """
This module contains all the common features of Hospital management.
    """,
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_patient_views.xml',
        'views/hospital_menuitem.xml',
    ],
    'demo': [],
    'sequence': -100,
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {},
    'license': 'LGPL-3',
}

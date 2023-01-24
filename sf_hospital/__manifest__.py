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
    'depends': [
        'mail',
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',

        'data/hospital_patient_tag_data.xml',
        'data/hospital.patient.tag.csv',

        'wizard/cancel_appointment_views.xml',

        'views/hospital_menuitem.xml',
        'views/hospital_appointment_views.xml',
        'views/hospital_patient_views.xml',
        'views/hospital_female_patient_views.xml',
        'views/hospital_patient_tag_views.xml',
    ],
    'demo': [],
    'sequence': -100,
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {},
    'license': 'LGPL-3',
}

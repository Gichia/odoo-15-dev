from odoo import fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Patient Name', required=True)
    ref = fields.Char(string='Reference')
    age = fields.Integer(string='Age')
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender')

from odoo import fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'

    name = fields.Char(string='Patient Name', required=True, tracking=True)
    ref = fields.Char(string='Reference')
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection(
        selection=[('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True)
    active = fields.Boolean(string='Active', default=True, tracking=True)

from datetime import date
from odoo import fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'

    name = fields.Char(string='Patient Name', required=True, tracking=True)
    ref = fields.Char(string='Reference')
    dob = fields.Date(string='Date Of Birth', required=True, tracking=True)
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True)
    gender = fields.Selection(
        selection=[('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True)
    active = fields.Boolean(string='Active', default=True, tracking=True)
    image = fields.Image(string='Image')

    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.dob:
                record.age = today.year - record.dob.year
            else:
                record.age = 0

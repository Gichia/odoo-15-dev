from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointments for patients'
    _rec_name = 'patient_id'

    patient_id = fields.Many2one(comodel_name='hospital.patient', string='Patient', required=True)
    gender = fields.Selection(string='Gender', related="patient_id.gender")
    appointment_time = fields.Datetime(string='Appointment Time', required=True)
    booking_date = fields.Date(string='Booking Date', required=True, default=fields.Date.today)
    ref = fields.Char(string='Reference', readonly=True)
    prescription = fields.Html(string='Prescription')

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

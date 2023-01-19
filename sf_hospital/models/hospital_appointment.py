from odoo import fields, models


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointments for patients'

    patient_id = fields.Many2one(comodel_name='hospital.patient', string='Patient', required=True)
    gender = fields.Selection(string='Gender', related="patient_id.gender")
    appointment_time = fields.Datetime(string='Appointment Time', required=True)
    booking_date = fields.Date(string='Booking Date', required=True, default=fields.Date.today)

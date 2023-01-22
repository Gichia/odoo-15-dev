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
    ref = fields.Char(string='Reference', readonly=True, help="Reference from patient record")
    prescription = fields.Html(string='Prescription')
    doctor_id = fields.Many2one(
        comodel_name='res.users', string='Doctor', required=True, tracking=True)
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], 
        string="Priority", help='Indicates the priority of the appointment.')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], 
        string="Status", default='draft', required=True, tracking=True)

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_confirm(self):
        for record in self:
            record.state = 'in_consultation'

    def action_done(self):
        for record in self:
            record.state = 'done'

    def action_cancel(self):
        for record in self:
            record.state = 'cancel'

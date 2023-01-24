from odoo import api, fields, models


class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string='Appointment')
    reason = fields.Text(string='Reason', required=True)

    def action_cancel_appointment(self):
        print(self)

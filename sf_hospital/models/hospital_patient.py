from datetime import date
from odoo import _, api, fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'

    name = fields.Char(string='Patient Name', required=True, tracking=True)
    ref = fields.Char(
        string='Order Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    dob = fields.Date(string='Date Of Birth', required=True, tracking=True)
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True)
    gender = fields.Selection(
        selection=[('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True)
    active = fields.Boolean(string='Active', default=True, tracking=True)
    image = fields.Image(string='Image')
    tag_ids = fields.Many2many(comodel_name='hospital.patient.tag', string='Tags')

    @api.model
    def create(self, vals):
        #Add your custom code here
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        return super(HospitalPatient, self).create(vals)

    def write(self, vals):
        #Add your custom code here
        # print('Writing::::::::::::')
        return super(HospitalPatient, self).write(vals)

    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.dob:
                record.age = today.year - record.dob.year
            else:
                record.age = 0


class HospitalPatientTag(models.Model):
    _name = 'hospital.patient.tag'
    _description = 'Hospital Patient Tags'

    name = fields.Char(string='Patient Tag', required=True, tracking=True)
    active = fields.Boolean(string='Active', default=True, tracking=True)
    color = fields.Integer(string='Color')

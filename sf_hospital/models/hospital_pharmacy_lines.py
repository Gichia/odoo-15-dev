from odoo import api, fields, models


class HospitalPharmacyLines(models.Model):
    _name = 'hospital.pharmacy.lines'
    _description = 'Appointment pharmacy lines for patients'

    product_id = fields.Many2one(
        comodel_name='product.product', string='Medicine', required=True, tracking=True)
    price_unit = fields.Float(string='Price')
    qty = fields.Integer(string='Quantity')
    appointment_id = fields.Many2one(
        comodel_name='hospital.appointment', string='Appointment')

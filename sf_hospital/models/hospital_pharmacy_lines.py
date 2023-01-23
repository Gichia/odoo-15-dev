from odoo import api, fields, models


class HospitalPharmacyLines(models.Model):
    _name = 'hospital.pharmacy.lines'
    _description = 'Appointment pharmacy lines for patients'

    product_id = fields.Many2one(
        comodel_name='product.product', string='Medicine', required=True)
    price_unit = fields.Float(string='Price', related='product_id.lst_price')
    qty = fields.Integer(string='Quantity', default=1)
    appointment_id = fields.Many2one(
        comodel_name='hospital.appointment', string='Appointment')

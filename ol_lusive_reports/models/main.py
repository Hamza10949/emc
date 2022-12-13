from odoo import models, fields,api
from odoo.exceptions import UserError
import base64
import requests
import datetime


class inheritincompany(models.Model):
    _inherit = 'mrp.production'


    psi = fields.Char(string='PSI')
    sample_collection = fields.Char(string='QA Sample Collected')
    technician = fields.Char(string='Technician')
    note = fields.Char(string='Note')

class inheritincompany(models.Model):
    _inherit = 'stock.picking'

    shipping_instruction = fields.Selection([('Overnight', 'Overnight'), ('SecondDay', 'Second Day'), ('Custom', 'Custom')])
    prepared_by = fields.Char(string='Prepared By')
    delivered_by = fields.Char(string='Delivered By')
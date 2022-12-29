from odoo import models, fields,api
from odoo.exceptions import UserError
import base64
import requests
import datetime


class inheritincompany(models.Model):
    _inherit = 'mrp.production'


    psi = fields.Char(string='PSG')
    sample_collection = fields.Char(string='QA Sample Collected')
    technician = fields.Char(string='Technician')
    notee = fields.Char(string='Note')
    plastic_source = fields.Char(string='Plastic Source')







class inheritincompanys(models.Model):
    _inherit = 'stock.picking'

    shipping_instruction = fields.Selection([('Overnight', 'Overnight'), ('SecondDay', 'Second Day'), ('Custom', 'Custom')])
    prepared_by = fields.Char(string='Prepared By')
    delivered_by = fields.Char(string='Delivered By')









class inheritinstockproductionlot(models.Model):
    _inherit = 'stock.production.lot'

    lot_traveller_ref = fields.Many2one('mrp.production', string="Lot Traveller Reference")



    def lot_traveller(self):
        reference = self.env['mrp.production'].search([('lot_producing_id','=', self.name)])
        self.lot_traveller_ref = reference.id
        return self.env.ref('ol_lusive_reports.report_lot_serial_ref').report_action(self)
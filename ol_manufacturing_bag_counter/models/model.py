
from odoo import models, api, fields, _
from odoo.exceptions import UserError




class extproduction(models.Model):
     _inherit = "mrp.production"
     ol_bags = fields.Char(compute='_compute_ol_bags', string='Bags')
     @api.depends('product_qty')
     def _compute_ol_bags(self):
        if self.bom_id:
            self.ol_bags=self.product_qty/self.bom_id.product_qty
        else:
            self.ol_bags=""

class extworkorder(models.Model):
    _inherit = "mrp.workorder"
    ol_bags = fields.Char(compute='_compute_ol_bags', string='Bags')
    psii = fields.Char(string='PSI', related='production_id.psi')
    sample_collection = fields.Char(string='QA Sample Collected', related = 'production_id.sample_collection')
    technician = fields.Char(string='Technician', related = 'production_id.technician')
    note = fields.Char(string='Note', related = 'production_id.note')
    plastic_source = fields.Char(string='Plastic Source', related = 'production_id.plastic_source')


    @api.depends('production_id')
    def _compute_ol_bags(self):
        if self.production_id:

            self.ol_bags=self.production_id.ol_bags
        else:

            self.ol_bags=""
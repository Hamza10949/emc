
from odoo import models, api, fields, _
from odoo.exceptions import UserError




class extproduction(models.Model):
     _inherit = "mrp.production"
     ol_bags = fields.Char(compute='_compute_ol_bags', string='Bags')
     
     @api.depends('product_qty')
     def _compute_ol_bags(self):
        self.ol_bags=self.product_qty/self.bom_id.product_qty

class extworkorder(models.Model):
    _inherit = "mrp.workorder"
    ol_bags = fields.Char(compute='_compute_ol_bags', string='Bags')

    @api.depends('')
    def _compute_ol_bags(self):
        self.ol_bags=self.production_id.ol_bags
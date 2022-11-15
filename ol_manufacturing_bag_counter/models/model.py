
from odoo import models, api, fields, _
from odoo.exceptions import UserError




class ext(models.Model):
     _inherit = "mrp.production"
     ol_bags = fields.Char(compute='_compute_ol_bags', string='Bags')
     
     @api.depends('product_qty')
     def _compute_ol_bags(self):
        self.ol_bags=self.product_qty/self.bom_id.product_qty
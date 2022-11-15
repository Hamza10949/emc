
from odoo import models, api, fields, _
from odoo.exceptions import UserError




class extproduction(models.Model):
     _inherit = "mrp.production"
     ol_bags = fields.Char(compute='_compute_ol_bags', string='Bags')
     
     @api.depends('product_qty')
     def _compute_ol_bags(self):
        if self.bom_id:
            self.ol_bags=self.product_qty/self.bom_id.product_qty

class extworkorder(models.Model):
    _inherit = "mrp.workorder"
    allow_producing_quantity_change = fields.Boolean('Allow Changes to Producing Quantity', default=True)
    ol_bags = fields.Char(compute='_compute_ol_bags', string='Bags')

    @api.depends('production_id')
    def _compute_ol_bags(self):
        if self.production_id:

            self.ol_bags=self.production_id.ol_bags
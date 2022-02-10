# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spaceships(models.Model):
    
    _name = 'space.spaceships'
    _description = 'Spaceships Management'
    
    name = fields.Char(string='Name', required=True)
    length = fields.Float(string='Lenght')
    height = fields.Float(string='Height')
    size = fields.Float(compute='_compute_dimension',readonly=True)
    fuel = fields.Char(string='Fuel Type')
    ship_type = fields.Char(string='Ship Type')
    number_passenger = fields.Integer(string='Number of passenger')
    model = fields.Char(string="Model")
    constructors = fields.Char(string="Constructor")
    isActive = fields.Boolean(string="Ready",default=False)
    status = fields.Selection(string='Statut',
                             selection=[('developement','In developpement'),
                                        ('in_progress','In Progress'),
                                        ('finished','Finished')],
                             copy=False)
    
    @api.depends('length','height')
    def _compute_dimension(self):
        for record in self:
            record.size= record.length * record.height
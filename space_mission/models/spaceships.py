# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError 

class Spaceships(models.Model):
    
    _name = 'space.spaceships'
    _description = 'Spaceships Management'
    
    name = fields.Char(string='Name', required=True)
    length = fields.Float(string='Lenght')
    width = fields.Float(string='Width')
    height = fields.Float(string='Height')
    size = fields.Float(compute='_compute_dimension',readonly=True, store=True)
    weight = fields.Float(string='Weight', compute='_calculate_ship_weight',readonly=True, store=True )
    number_engine = fields.Integer(string='Number of engine (1/680t)',compute='_number_of_engine_needed',readonly=True, store=True)
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
    
    mission_id = fields.One2many(comodel_name='space.missions', inverse_name='spaceship_ids', string='Mission')
    
    @api.depends('length','width','height')
    def _compute_dimension(self):
        for record in self:
            record.size= record.length * record.width * record.height
    
    @api.constrains('length','width')
    def _height_verification_inferior(self):
        for record in self:
            if record.length > record.width:
                raise ValidationError("Height can't be superior than Length !")
            else:
                continue

    @api.depends('size')
    def _calculate_ship_weight(self):
        for record in self:
            if record.size:
                record.weight = (record.size * (2/7))
            else:
                continue
                
    @api.depends('weight')
    def _number_of_engine_needed(self):
        for record in self:
            if record.weight:
                num_engine = record.weight/680
                if num_engine >= int(num_engine):
                    record.number_engine = int(num_engine) + 1
                else:
                    record.number_engine = int(num_engine)
            else:
                continue
                    
                
                
               
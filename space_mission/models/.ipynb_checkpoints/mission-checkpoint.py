# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError 

class SpaceMissions(models.Model):
    
    _name = 'space.missions'
    _description = 'Global Mission in Space'
    
    name = fields.Char(string='Mission', required=True)
    spaceship_ids = fields.Many2one(comodel_name='space.spaceships', string='Ships', ondelete='cascade', required=True)
    destination = fields.Selection(string='Destination', selection=[('mars','Mars'),('jupiter','Jupiter'),('saturn','Saturne'),('uranus','Uranus'),('neptune','Neptune')])
    launch_date = fields.Date(string='Launch date')
    return_date = fields.Date(string='Return date')
    ship_status = fields.Selection(string='Ships State', related='spaceship_ids.status', readonly=True)
    ship_number_passenger = fields.Integer(string='Ships Number Passenger', related='spaceship_ids.number_passenger', readonly=True, store=True)
    ship_number_engine = fields.Integer(string='Ships Number Engine', related='spaceship_ids.number_engine', readonly=True, store=True)
    crew_member_ids = fields.Many2many(comodel_name='res.partner', string='Crew Members', domain=[('company_type', '=', 'person')])
    fuel_ship = fields.Char(string='Fuel', related='spaceship_ids.fuel', readonly=True)
    travel_distance = fields.Integer('Travel distance', compute='_fuel_quantity_needed', readonly=True, store=True)
    fuel_needed = fields.Integer('Fuel Needed', compute='_fuel_calculation', readonly=True, store=True)
    project_id = fields.One2many(comodel_name='project.task', inverse_name='mission_ids', string='Project')
    
    @api.depends('destination')
    def _fuel_quantity_needed(self):
        for record in self:
            if record.destination:
                destination = record.destination
                if destination == 'mars':
                    record.travel_distance = 62
                elif destination == 'jupiter':
                    record.travel_distance = 628
                elif destination == 'saturn':
                    record.travel_distance = 1658
                elif destination == 'uranus':
                    record.travel_distance = 2300
                elif destination == 'neptune' :
                    record.travel_distance = 4300
            else:
                record.travel_distance = 0
                
    @api.depends('ship_number_engine')
    def _fuel_calculation(self):
        for record in self:
            if record.ship_number_engine:
                record.fuel_needed = record.ship_number_engine * 14000
            else:
                continue
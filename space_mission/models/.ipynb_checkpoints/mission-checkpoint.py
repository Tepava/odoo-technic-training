from odoo import models, fields, api
from odoo.exceptions import ValidationError 

class SpaceMissions(models.Model):
    
    _name = 'space.missions'
    _description = 'Global Mission in Space'
    
    name = fields.Char(string='Name', required=True)
    spaceship_ids = fields.Many2one(comodel_name='space.spaceships', string='Ships', ondelete='cascade', required=True)
    destination = fields.Selection(string='Destination', selection=[('mars','Mars'),('jupiter','Jupiter'),('saturn','Saturne'),('uranus','Uranus'),('neptune','Neptune')])
    launch_date = fields.Date(string='Launch date')
    return_date = fields.Date(string='Return date')
    ship_status = fields.Selection(string='Ships State', related='spaceship_ids.status', readonly=True)
    crew_member_ids = fields.Many2many(comodel_name='res.partner', string='Crew Members', domain=[('company_type', '=', 'person')])
    fuel_ship = fields.Char('Fuel', related='spaceship_ids.fuel', readonly=True)
    travel_distance = fields.Integer('Travel distance', readonly=True)
    fuel_needed = fields.Integer('Fuel Needed', readonly=True)
    
    
    @api.onchange('destination')
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
        
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SpaceProject(models.Model):
    _inherit = 'project.task'
    
    mission_ids = fields.Many2one(string='Missions', comodel_name='space.missions', ondelete='set null')
    ship_state = fields.Selection(string='Ship Status', related='mission_ids.ship_status')
    ship_id = fields.Many2one(string='Ship', related='mission_ids.spaceship_ids', readonly=True)
    ship_name = fields.Char(string='Ship Name', related='ship_id.name', readonly=True)
    
    
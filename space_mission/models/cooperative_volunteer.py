# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CooperativeVolunteers(models.Model):
    
    _name = 'space.cooperative.volunteers'
    _description = 'Task for Volunteers'
    
    name = fields.Char(string='Name', required=True)
    task_type = fields.Char(string='Type')
    task_description = fields.Text(string='Task description')
    start_time = fields.Datetime(string='Start Time')
    #start_time = fields.Float(string='Time', compute="_compute_start_time")
    stop_time = fields.Datetime(string='Stop Time')
    #stop_time = fields.Float(string='Time', compute="_compute_end_time")
    task_repeat = fields.Boolean(string='Repeat Task', default=False)
    frequency = fields.Integer(string='Number of repetition', default=0)
    #will be replace after by user with a related fields
    #volunteer = fields.Selection(string='Volunteer', selection=[('1','Finéas'),('2','Andrew'),('3','Rosa')])
    volunteer_ids = fields.Many2one(string='Volunteer', comodel_name='res.partner', required=True)
    leader = fields.Selection(string='Leader', selection=[('1','Finéas'),('2','Andrew'),('3','Rosa')])
    state = fields.Selection(string='State',selection=[('draft','Draft'),('ready','Ready'),('in_progress','In Progress'),('finished','Finished')], default='draft')
    
    
    @api.onchange('leader')
    def _state_status(self):
        for record in self:
            if record.leader and record.state == 'draft':
                record.state = 'ready'
    
    
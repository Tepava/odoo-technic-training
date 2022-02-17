# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CooperativeVolunteers(models.Model):
    
    _name = 'space.cooperative.volunteers'
    _description = 'Task for Volunteers'
    
    name = fields.Char(string='Name', required=True)
    task_type = fields.Char(string='Type')
    task_description = fields.Text(string='Task description')
    start_time = fields.Datetime(string='Start Time')
    stop_time = fields.Datetime(string='Stop Time')
    task_repeat = fields.Boolean(string='Repeat Task', default=False)
    frequency = fields.Integer(string='Number of repetition', default=0)
    volunteer_ids = fields.Many2one(string='Volunteer', comodel_name='res.partner', required=True)
    leader = fields.Selection(string='Leader', selection=[('1','Finéas'),('2','Andrew'),('3','Rosa')])
    state = fields.Selection(string='State',selection=[('draft','Draft'),('ready','Ready'),('in_progress','In Progress'),('finished','Finished')], default='draft')
    approval_ids = fields.One2many(string='Task',comodel_name='approval.request', inverse_name='task_ids')
    
    @api.onchange('leader')
    def _state_status(self):
        for record in self:
            if record.leader and record.state == 'draft':
                record.state = 'ready'
    
    
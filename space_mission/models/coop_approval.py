# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CooperativeApproval(models.Model):
    _inherit ='approval.request'
    
    task_ids = fields.Many2one(string='Approvals', comodel_name='space.cooperative.volunteers')
    
    @api.onchange('task_ids')
    def _auto_period_fill(self):
        for record in self:
            if record.task_ids:
                record.date_start = record.task_ids.start_time
                record.date_end = record.task_ids.stop_time
            else:
                continue
                

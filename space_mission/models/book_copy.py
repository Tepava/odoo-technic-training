# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryCopy(models.Model):
    
    _name = 'space.library.copy'
    _description = 'Books Copy'
    
    _inherits = {
        'space.library':'book_ids'
    }
    
    book_ids = fields.Many2one(string='Origin ID', comodel_name='space.library', required=True, ondelete='cascade')
    book_reference = fields.Char(string='Book_reference',)
    book_available = fields.Boolean(string='Available', default='False', readonly=True)
    
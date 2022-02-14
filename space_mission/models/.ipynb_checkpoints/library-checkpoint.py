# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Library(models.Model):
    
    _name = 'space.library'
    _description = 'Library'
    
    name = fields.Char(string='Book Name')
    author = fields.Char(string='Author')
    editor = fields.Char(string='Editor')
    publisher = fields.Char(string='Publisher')
    year_edition = fields.Char(string='Year')
    isbn = fields.Char(string='ISBN')
    genre = fields.Char(string='Genre')
    book_note = fields.Text(string="Book Note")
    
    @api.onchange('isbn')
    def _isbn_size_limite(self):
        _logger = logging.getLogger(__name__)
        for record in self:
            if record.isbn and len(record.isbn) > 13:
                raise ValidationError("The ISBN size can't be superior of 13")
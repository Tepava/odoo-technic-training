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
    books_copy_ids = fields.One2many(string='Book Copy',  inverse_name='book_ids',comodel_name='space.library.copy')
    number_of_copy = fields.Integer(string='Number of Copy', compute='_calcul_of_number_of_copy')
    
    @api.onchange('isbn')
    def _isbn_size_limite(self):
        _logger = logging.getLogger(__name__)
        for record in self:
            if record.isbn and len(record.isbn) > 13:
                raise ValidationError("The ISBN size can't be superior of 13")
    
    @api.depends('books_copy_ids')
    def _calcul_of_number_of_copy(self):
        for record in self:
            record.number_of_copy = len(record.books_copy_ids)
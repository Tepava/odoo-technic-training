# -*- coding: utf-8 -*-

from odoo import models, fields, api
    
class Library(models.Model):
    
    _name = 'space.library'
    _description = 'Library'
    
    name = fields.Char(string='Book Name')
    author = fields.Char(string='Author')
    editor = fields.Char(string='Editor')
    publisher = fields.Char(string='Publisher')
    year_edition = fields.Integer(string='Year')
    isbn = fields.Char(string='ISBN')
    genre = fields.Char(string='Genre')
    
    
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    
    _name = 'space.book'
    _description = 'Library Management'
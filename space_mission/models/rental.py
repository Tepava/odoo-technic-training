from odoo import models, fields, api
from odoo.exceptions import ValidationError 

class LibraryRental(models.Model):
    
    _name = 'space.library.rental'
    _description = 'Manage library rental'
    
    name = fields.Char(string='CodeName')
    book_ids = fields.Many2one(string='Book', comodel_name='space.library', required=True)
    book_id = fields.Integer(string='Book ID', related='book_ids.id')
    book_name = fields.Char(string='Book Name', related='book_ids.name')
    customer_ids = fields.Many2one(string='Customer', comodel_name='res.partner', required=True)
    customer_name = fields.Char(string='Customer Name', related='customer_ids.name')
    
    date_rental = fields.Date(string='Date of rental')
    date_return = fields.Date(string='Date of return')
    
    ###################WIP##########################################
    #@api.onchange('book_id','customer_name')
    #def _code_name_rental(self):
    #    last_id = max(self.env('space.library.rental').search([]))
    #    book_id = str(record.book_id) 
    #    for record in self:
    #        if last_id[0] < 1:
    #            last_id[0] = 1
    #            if book_id and last_id:
    #                record.name = "RENT"+ book_id +""+ last_id[0]

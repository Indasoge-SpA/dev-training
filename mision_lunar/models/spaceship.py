# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spaceship(models.Model):
    
    _name = 'academy.spaceship'
    _description = 'A Space Ship'
    
    name_id=fields.Char(string='Identifier', required=True)
    description =fields.Text(string='Common Name')
    
    length = fields.Float(string='Length', required=True)
    width  = fields.Float(string='Width', required=True)
    depth  = fields.Float(string='Depth', required=True)
    
    fuel_type = fields.Selection(string='Fuel Type', required=True,
                                selection=[('solid','Solid'),
                                           ('liquid','Liquid')],
                                copy=False,default='solid')
    
    ship_type = fields.Selection(string='Ship Type', required=True,
                                selection=[('commercial', 'Commercial'),
                                          ('cargo','Cargo'),
                                          ('batleship','BatleShip')],
                                copy=False, default='cargo')
    crew_number = fields.Integer(string='Crew Dotation', required=True)
    passanger_number = fields.Integer(string='Number of Passangers', required=True)
    
    active = fields.Selection(string='Active', required=True, 
                              selection=[('active','Active'),
                                        ('retired','Retired')],
                              copy=False,default='active')
    
    
    
# -*- coding: utf-8 -*-

from odoo import models, fields, api
print("Class def")
class spaceship(models.Model):
    
    _name = 'exploration.spaceship'
    _description = 'exploration.spaceship'
    
    name=fields.Char(string='name', required=True)
    code=fields.Char(string='code',requerid=True)
    description =fields.Text(string='Common Name')
    
    release_date=fields.Date(string='Manufacturing Year',required=True)
    length = fields.Float(string='Length', required=True)
    width  = fields.Float(string='Width', required=True)
    heigth  = fields.Float(string='Heigth', required=True)
    
    fuel_type = fields.Selection(string='Fuel Type', required=True,
                                selection=[('solid','Solid'),
                                           ('liquid','Liquid')],
                                copy=False,default='solid')
    
    ship_type = fields.Selection(string='Ship Type', required=True,
                                selection=[('commercial', 'Commercial'),
                                          ('cargo','Cargo'),
                                          ('battleship','BattleShip')],
                                copy=False, default='cargo')
    crew_number = fields.Integer(string='Crew Dotation', required=True)
    passanger_number = fields.Integer(string='Number of Passangers', required=True)
    
    active = fields.Selection(string='Active', required=True, 
                              selection=[('active','Active'),
                                        ('retired','Retired')],
                              copy=False,default='active')
print("class out")
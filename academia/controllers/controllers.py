# -*- coding: utf-8 -*-
# from odoo import http


# class Spaceship(http.Controller):
#     @http.route('/spaceship/spaceship/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/spaceship/spaceship/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('spaceship.listing', {
#             'root': '/spaceship/spaceship',
#             'objects': http.request.env['spaceship.spaceship'].search([]),
#         })

#     @http.route('/spaceship/spaceship/objects/<model("spaceship.spaceship"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('spaceship.object', {
#             'object': obj
#         })

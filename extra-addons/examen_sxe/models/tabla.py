# -*- coding: utf-8 -*-

from odoo import fields, models

class TestModel(models.Model):
    _name = "model"
    _description = "model"

    id = fields.Integer(string="ID")
    producto = fields.Char(string="Producto")
    viabilidad = fields.Float(string="Viabilidad")
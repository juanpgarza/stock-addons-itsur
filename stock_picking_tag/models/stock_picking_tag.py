# Copyright 2021 ITSur - Juan Pablo Garza <jgarza@itsur.com.ar>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class StockPickingTag(models.Model):
    _name = 'stock.picking.tag'
    _description = "Tag Transferencias"

    name = fields.Char('Nombre', required=True, translate=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "El tag ya existe !"),
    ]
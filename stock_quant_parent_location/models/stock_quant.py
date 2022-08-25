# Copyright 2022 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    parent_location_id = fields.Many2one(string="Ubicación Padre", related='location_id.location_id', store=True)
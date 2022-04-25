# Copyright 2021 ITSur - Juan Pablo Garza <jgarza@itsur.com.ar>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def change_picking_type(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Cambiar el tipo de operación',
            'view_mode': 'form',
            'res_model': 'change.picking.type.wizard',
            'target': 'new'  
        }
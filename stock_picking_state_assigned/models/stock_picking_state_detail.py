##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api


class StockPickingStateDetail(models.Model):
    _inherit = 'stock.picking.state_detail'

    end_state = fields.Boolean("sub estado final")
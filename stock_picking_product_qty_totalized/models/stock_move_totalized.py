# Copyright 2021 ITSur - Juan Pablo Garza <jgarza@itsur.com.ar>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime
from odoo.addons import decimal_precision as dp

class StockMoveTotalized(models.Model):
    _name = 'stock.move.totalized'
    _description = 'Cantidad total por producto'

    picking_id = fields.Many2one(
        'stock.picking', 'Stock Picking', auto_join=True,
        help='The stock operation where the packing has been made')

    qty = fields.Float('Cantidad', default=0.0, digits=dp.get_precision('Product Unit of Measure'), copy=False)

    product_id = fields.Many2one('product.product', 'Producto', ondelete="cascade")


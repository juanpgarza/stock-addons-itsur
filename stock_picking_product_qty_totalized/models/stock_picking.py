# Copyright 2021 ITSur - Juan Pablo Garza <jgarza@itsur.com.ar>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    move_ids_totalized = fields.One2many('stock.move.totalized', 
                                            'picking_id', 
                                            string="Movimientos totalizados por producto")

        # product_uom_qty  
        # reserved_availability
        # quantity_done

    def _calcular_agrupado(self):
        agrupado = {}
        for move in self.move_lines.filtered(lambda x: x.state != 'cancel'):

            cantidad = 0
            if self.state == 'done':
                cantidad = move.quantity_done
            else:
                cantidad = move.reserved_availability

            if move.product_id.id not in agrupado:
                agrupado[move.product_id.id] = {'qty': cantidad}
            else:
                agrupado[move.product_id.id]['qty'] += cantidad

        # import pdb; pdb.set_trace()
        
        move_totalized = self.env['stock.move.totalized']
        move_totalized.search([('picking_id','=',self.id)]).unlink()
        for key in agrupado:
            move_totalized.create({
                            'picking_id': self.id, 
                            'product_id': key, 
                            'qty': agrupado[key]['qty']
                            })

    @api.multi
    def action_assign(self):
        super(StockPicking, self).action_assign()
        self._calcular_agrupado()

    @api.multi
    def action_done(self):
        super(StockPicking, self).action_done()       
        self._calcular_agrupado()
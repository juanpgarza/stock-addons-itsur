# Copyright 2021 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def create(self,values):
        # import pdb; pdb.set_trace()
        res = super(StockPicking,self).create(values)
        res.state_detail_id = self.env.ref('stock_picking_state_assigned.picking_state_detail_reservado')
        return res

    @api.multi
    def button_validate(self):
        # import pdb; pdb.set_trace()
        if not self.state_detail_id.end_state:
            # import pdb; pdb.set_trace()
            # le tengo que asignar el siguiente estado en la secuencia
            state_detail_id = self.env['stock.picking.state_detail'].search([('sequence','=',self.state_detail_id.sequence + 1)])

            self.write({
                'state_detail_id': state_detail_id.id
            })
            # import pdb; pdb.set_trace()
        else:
            return super(StockPicking,self).button_validate()

    # @api.multi
    # def button_validate(self):
    #     return super(StockPicking,self).button_validate()

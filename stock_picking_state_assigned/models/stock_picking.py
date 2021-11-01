# Copyright 2021 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.exceptions import ValidationError
from odoo import models, fields, api, _
from odoo.tools import float_compare

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    state_detail_user_id = fields.Many2one(
        'res.users', string='Usuario que modificó el subestado',track_visibility='always')

    @api.model
    def _default_state(self):
        return self.env.ref('stock_picking_state_assigned.picking_state_detail_reservado')        

    @api.model
    def create(self,values):
        # import pdb; pdb.set_trace()
        res = super(StockPicking,self).create(values)
        res.state_detail_id = self._default_state()
        return res

    @api.multi
    def button_validate(self):
        # import pdb; pdb.set_trace()
        if self.state_detail_id:
            if self.state_detail_id.next_state():

                # si el próximo estado es final, le tengo que exigir que todo lo reservado este hecho
                if not self.state_detail_id.next_state().next_state():
                    if any(self.move_line_ids.filtered(lambda x: x.state not in ['draft', 'done', 'cancel']).filtered(lambda y: y.product_uom_qty != y.qty_done)):
                        raise ValidationError("Todo debe estar como hecho")

                # le tengo que asignar el siguiente estado en la secuencia
                self.write({
                    'state_detail_id': self.state_detail_id.next_state().id,
                    'state_detail_user_id': self.env.uid
                })
                # import pdb; pdb.set_trace()
            else:
                return super(StockPicking,self).button_validate()
        else:
            return super(StockPicking,self).button_validate()

    @api.model
    def _assign_default_state(self):
        for aaa in self.with_context(active_test=False).search(
                [('state_detail_id', '=', False)]):
            aaa.state_detail_id = self._default_state()

    @api.multi
    def write(self, values):
        if 'state_detail_id' in values:
            # si tenía un subestado informado (ej. para armar o armado) y el próximo estado es reservado, marcar todo como sin realizar.
            if self.state_detail_id and self.env.ref('stock_picking_state_assigned.picking_state_detail_reservado').id == values["state_detail_id"]:
                self.move_line_ids.filtered(lambda x: x.state not in ['draft', 'done', 'cancel']).write({'qty_done': False})
                # import pdb; pdb.set_trace()
            values["state_detail_user_id"] = self.env.uid
        if 'state' in values:
            if values["state"] == 'done' and self.state_detail_user_id.id == self.env.uid:
                raise ValidationError("El usuario que preparó el pedido no puede ser el mismo que válida su entrega")
        super(StockPicking,self).write(values)
        
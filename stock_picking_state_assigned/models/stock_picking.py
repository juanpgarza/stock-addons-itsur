# Copyright 2021 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.exceptions import ValidationError
from odoo import models, fields, api, _
from odoo.tools import float_compare

class StockPicking(models.Model):
    _inherit = 'stock.picking'

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
                    'state_detail_id': self.state_detail_id.next_state().id
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
        super(StockPicking,self).write(values)

    def _check_sale_paid(self):        
        if self.state_detail_id.next_state():
            return True
        else:
            # super(StockPicking,self)._check_sale_paid()
            # tuve que sobreescribir _check_sale_paid porque no funcionaba
            precision = self.env['decimal.precision'].precision_get(
                'Product Unit of Measure')
            invoice_status = self.sale_id.mapped(
                'order_line.invoice_lines.invoice_id.state')
            if (set(invoice_status) - set(['paid'])) or any(
                    (float_compare(line.product_uom_qty,
                                line.qty_invoiced,
                                precision_digits=precision) > 0)
                    for line in self.sale_id.order_line):
                return False
            return True        
# Copyright 2021 ITSur - Juan Pablo Garza <jgarza@itsur.com.ar>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    stock_picking_log_ids = fields.One2many('stock.picking.log', 
                                            'picking_id', 
                                            string="Logs de la transferencia")

    @api.multi
    def write(self, values):     
        super(StockPicking,self).write(values)

        # 1 #
        self.stock_picking_log_ids.filtered(lambda x: x.log_type == 'ubicacion_origen').unlink()        
        if self.location_id and self.location_id != self.picking_type_id.default_location_src_id:
            self.create_log("Ubicación origen no coincide","ubicacion_origen")

        # 2 #
        self.stock_picking_log_ids.filtered(lambda x: x.log_type == 'ubicacion_destino').unlink()        
        if self.picking_type_id.code in ('internal','incoming') and self.location_dest_id != self.picking_type_id.default_location_dest_id:
            self.create_log("Ubicación destino no coincide","ubicacion_destino")

        # 3 #
        self.stock_picking_log_ids.filtered(lambda x: x.log_type == 'en_clima').unlink()        
        if self.sale_id and self.sale_id.type_id.en_clima:
            self.create_log("Operación en clima","en_clima")

        # 4 #
        self.stock_picking_log_ids.filtered(lambda x: x.log_type == 'entrega_sin_pedido').unlink()        
        if self.picking_type_id.code == 'outgoing' and not self.sale_id:
            self.create_log("Orden de entrega sin pedido","en_clima")

    def create_log(self, description, log_type):

        vals = {
            'picking_id': self.id,
            'fecha_hora': fields.Datetime.now(),
            'description': description,
            'log_type': log_type
        }
        
        log = self.env['stock.picking.log'].create(vals)
        # import pdb; pdb.set_trace()
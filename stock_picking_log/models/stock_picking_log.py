# Copyright 2021 ITSur - Juan Pablo Garza <jgarza@itsur.com.ar>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class StockPickingLog(models.Model):
    _name = 'stock.picking.log'
    _description = 'Logs de transferencias'

    fecha_hora = fields.Datetime(String="Fecha/Hora Log")
    picking_id = fields.Many2one('stock.picking', string="Transferencia")
    description = fields.Char(string="Descripción")
    log_type = fields.Selection(
                            [
                            ('ubicacion_origen','Ubicación origen no coincide'),
                            ('ubicacion_destino','Ubicación destino no coincide'),
                            ('en_clima','Operación en clima'),
                            ('entrega_sin_pedido','Orden de entrega sin pedido'),
                            ('otro','Otro'),
                            ],'Tipo')
##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api


class StockPickingStateDetail(models.Model):
    _inherit = 'stock.picking.state_detail'

    # end_state = fields.Boolean("sub estado final")

    @api.multi
    def next_state(self):

        estados = self.env["stock.picking.state_detail"].search([('state','=','assigned')])

        secuencia = estados.mapped('sequence')

        secuencia.sort()

        indice = secuencia.index(self.sequence)

        if len(secuencia) == indice + 1:
            # ultimo estado
            return False
        else:
            return self.env["stock.picking.state_detail"].search([('state','=','assigned'),('sequence','=',secuencia[indice+1])])
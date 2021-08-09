# Copyright 2021 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def create(self,values):
        # import pdb; pdb.set_trace()
        res = super(StockPicking,self).create(values)
        res.state_detail_id = 1
        return res

    @api.multi
    def button_validate(self):
        # import pdb; pdb.set_trace()
        if self.state_detail_id.id == 1:
            # self.state_detail_id = 2
            self.write({
                'state_detail_id': 2
            })
            # import pdb; pdb.set_trace()
        else:
            return super(StockPicking,self).button_validate()

    # @api.multi
    # def button_validate(self):
    #     return super(StockPicking,self).button_validate()

from odoo import models, fields, api
from odoo.exceptions import UserError

class ChangePickingtypeWizard(models.TransientModel):
    _name = 'change.picking.type.wizard'
    _description = 'Cambiar el tipo de operación'

    picking_id = fields.Many2one('stock.picking')

    picking_type_id = fields.Many2one('stock.picking.type', string='Tipo')

    @api.model
    def default_get(self, field_names):
        defaults = super(
            ChangePickingtypeWizard, self).default_get(field_names)
        defaults['picking_id'] = self.env.context['active_id']
        return defaults

    def do_update(self):        

        if self.picking_id.state != 'draft':
            raise UserError("Solo en borrador")

        if self.picking_id.picking_type_id.id == self.picking_type_id.id:
            raise UserError("Indique un tipo de operación distinto al actual")

        self.picking_id.write(
            {
            'name': self.picking_type_id.sequence_id.next_by_id(),
            'picking_type_id': self.picking_type_id.id,
            'location_id': self.picking_type_id.default_location_src_id.id,            
            }
        )

        for move in self.picking_id.move_ids_without_package:
            move.write(
                {
                    'location_id': self.picking_type_id.default_location_src_id.id,
                }
            )
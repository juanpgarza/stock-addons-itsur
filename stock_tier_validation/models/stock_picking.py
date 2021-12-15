# Copyright 2019 Open Source Integrators
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class StockPicking(models.Model):
    _name = "stock.picking"
    _inherit = ['stock.picking', 'tier.validation']
    _state_from = ['assigned', 'waiting', 'confirmed']
    _state_to = ['done']

    review_done_by_users = fields.Char(string='Aprobado Por',compute="_compute_review_user_ids",store=True)

    @api.depends('review_ids')
    def _compute_review_user_ids(self):
        for rec in self:
            if rec.review_ids:
                rec.review_done_by_users = ', '.join(rec.review_ids.mapped("done_by.name"))
            else:
                rec.review_done_by_users = False
    
    def action_done(self):
        self.write({'state': 'done'})
        res = super().action_done()
        return res

    def _notify_accepted_reviews(self):
        return super(StockPicking, self.sudo())._notify_accepted_reviews()

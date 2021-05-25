# Copyright 2021 ITSur - Juan Pablo Garza <jgarza@itsur.com.ar>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "stock_picking_product_qty_totalized",
    "summary": "",
    "version": "12.0.1.0.0",
    "category": "Stock",
    "website": "https://github.com/itsurnqn/account-addons",
    "author": "ITSur",
    "license": "AGPL-3",
    "depends": ["stock","sale"],
    "data": [
        'views/stock_picking_views.xml',
        'security/ir.model.access.csv',
        'reports/report_stockpicking_operations.xml'        
        ],
    "installable": True,
}

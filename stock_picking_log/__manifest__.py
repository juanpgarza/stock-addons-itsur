# Copyright 2021 ITSur - Juan Pablo Garza <jgarza@itsur.com.ar>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "stock_picking_log",
    "summary": "",
    "version": "12.0.1.0.0",
    "category": "Stock",
    "website": "https://github.com/itsurnqn/stock-addons",
    "author": "ITSur",
    "license": "AGPL-3",
    "depends": ["stock","sale_order_type"],
    "data": [
        'views/sale_order_type_views.xml',        
        'views/stock_picking_views.xml',
        'security/ir.model.access.csv',
        ],
    "installable": True,
}

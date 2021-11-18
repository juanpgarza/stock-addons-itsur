# Copyright 2021 ITSur - Juan Pablo Garza <jgarza@itsur.com.ar>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "stock_picking_tag",
    "summary": "",
    "version": "12.0.1.0.0",
    "category": "Stock",
    "website": "https://github.com/itsurnqn/stock-addons",
    "author": "ITSur",
    "license": "AGPL-3",
    "depends": ["stock"],
    "data": [
        'views/stock_picking_views.xml',
        'views/stock_picking_tag_views.xml',        
        'security/ir.model.access.csv',
        ],
    "installable": True,
}

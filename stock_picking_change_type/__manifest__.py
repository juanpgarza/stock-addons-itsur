# Copyright 2022 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "stock_picking_change_type",
    "summary": "",
    "version": "12.0.1.0.0",
    "category": "Stock",
    "website": "https://github.com/itsurnqn/stock-addons",
    "author": "juanpgarza",
    "license": "AGPL-3",
    "depends": ["stock"],
    "data": [
        'views/stock_picking_views.xml',        
        'wizards/change_picking_type_views.xml',
        ],
    "installable": True,
}

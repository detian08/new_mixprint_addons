# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012 - INECO PARTNERSHIP LIMITE (<http://www.ineco.co.th>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name' : 'INECO STOCK',
    'version' : '0.1',
    'depends' : ['base','sale','stock','sale_stock','purchase','mrp','product'],
    'author' : 'Mr.Tititab Srisookco',
    'category': 'INECO',
    'description': """
Stock module addon.
1. Please update query after install this modules
    ALTER TABLE STOCK_MOVE DROP CONSTRAINT IF EXISTS stock_move_move_dest_id_fkey;
    DROP INDEX IF EXISTS stock_move_move_dest_id_index;

    """,
    'website': 'http://www.ineco.co.th',
    'data': [],
    'update_xml': [
        'stock_view.xml',
        'sale_view.xml', 
        'product_view.xml',
        'stock_report_view.xml',
        'stock_lot_issue_view.xml',
        'stock_barcode_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'images': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
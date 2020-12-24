# -*- coding: utf-8 -*-
{
    'name': "Report Sale Details",

    "author": "Marouf Alktheeri",

    "version" : "13.0.1",

    "support": "marouftk2020@gmail.com", 

    "category": "Point Of Sale",

	"summary": """print sale details report app, print Sale Details report odoo""",

	"description": """This module useful to print sale details report app, print Sale details report odoo""",

    'depends': ['point_of_sale'],

    'css':'static/src/css/styel.css',

    'data': [
        'reports/pos_saledetiles_inhet.xml',  
    ],

	"installable": True,
	"application": True,
	"auto_install": False,
}

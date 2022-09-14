# -*- coding: utf-8 -*-
{
    'name': "Módulo-La Ilusion",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Este modulo modifica el Reporte de Factura Electronica segun las especificaciones del cliente
    """,

    'author': "Nelson Velez",
    'website': "http://www.intresco.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '12.1',

    # any module necessary for this one to work correctly
    'depends': ['l10n_co_tax_extension','l10n_co_e-invoice'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
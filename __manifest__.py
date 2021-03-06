# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Customer Outstanding Statement',
    'version': '10.0.1.1.0',
    'category': 'Accounting & Finance',
    'summary': 'OCA Financial Reports',
    'author': "Eficent, Odoo Community Association (OCA)",
    'website': 'https://github.com/OCA/account-financial-reporting',
    'license': 'AGPL-3',
    'depends': [
        'account','sh_account_edit_seq',
    ],
    'data': [
        'views/statement.xml',
        'views/new_account_move.xml',
        'wizard/customer_outstanding_statement_wizard.xml',
    ],
    'installable': True,
    'application': False,
}

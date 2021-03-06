# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012-2015 Bluestar Solutions Sàrl (<http://www.blues2.ch>).
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
    'name': 'Test Warning',
    'version': '7.0.2.3-20160509',
    "category": 'Bluestar/Generic web module',
    'complexity': "easy",
    'description': """
Warning style for staging/testing install
=========================================

Flashy look and feel for OpenERP web interface to not mix up your production
instance with your staging/testing instance.
    """,
    'author': 'Bluestar Solutions Sàrl',
    'website': 'http://www.blues2.ch',
    'depends': ['web'],
    "js": [],
    "css": ['static/src/css/test_warning.css'],
    'auto_install': False,
    'web_preload': False,
    'images': ['images/web_test_warning.png', ],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

#############################################################################
##                                                                         ##
##  Copyleft by WebNuLL < webnull.www at gmail dot com >                   ##
##                                                                         ##
## This program is free software; you can redistribute it and/or modify it ##
## under the terms of the GNU General Public License version 3 as          ##
## published by the Free Software Foundation; version 3.                   ##
##                                                                         ##
## This program is distributed in the hope that it will be useful, but     ##
## WITHOUT ANY WARRANTY; without even the implied warranty of              ##
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU       ##
## General Public License for more details.                                ##
##                                                                         ##
#############################################################################

class alangINC():
	def return_array(a):
		MyLang = range(11)
		MyLang[1] = 'Shutdown'
		MyLang[2] = 'Reboot'
		MyLang[3] = 'Logout'
		MyLang[4] = 'Lock screen'
		MyLang[5] = 'Exit Session'
		MyLang[6] = '[xsm-gui.py] No xscreensaver found to be running, disabling #btn4 with Locking screen option'
		MyLang[7] = 'Hibernate'
		MyLang[8] = 'Sleep'
		MyLang[9] = 'Quick restart'
		MyLang[10] = 'Reload currently running operating system'
		return MyLang

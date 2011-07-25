#-*- coding: utf-8 -*-

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
                MyLang[1] = 'Wyłącz komputer'
                MyLang[2] = 'Uruchom ponownie'
                MyLang[3] = 'Wyloguj'
                MyLang[4] = 'Zablokuj ekran'
                MyLang[5] = 'Zakończ sesję'
                MyLang[6] = '[xsm-gui.py] Aplikacja xscreensaver nie została odnaleziona wśrod procesów systemowych, funkcja blokowania ekranu zostanie wyłączona.'
                MyLang[7] = 'Zahibernuj'
                MyLang[8] = 'Uśpij'
                MyLang[9] = 'Szybki restart'
                MyLang[10] = 'Załaduj ponownie bieżący system operacyjny'
                return MyLang

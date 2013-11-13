#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sin título.py
#  
#  Copyright 2013 Carlos Arturo Guerra Parra <carlos@carlos-TravelMate-P253>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import temperamentos as tem

def creditos():
	print "Carlos Arturo Guerra Parra"
	print "carlosarturoguerra@gmail.com"
	print "2013"
	
comandos = { 'creditos' : creditos }


def main():
		
	sentencia = ""
	while sentencia != "exit":
		sentencia = raw_input("temp >>> ")
		palabras = sentencia.split()
		if palabras[0] in comandos:
			comandos[palabras[0]]()	
	
	
	return 0

if __name__ == '__main__':
	main()


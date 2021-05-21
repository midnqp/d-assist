''' 
Codebase Automated Documentation
Copyright (C) 2021 Muhammad Bin Zafar <midnightquantumprogrammer@gmail.com>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, see <http://gnu.org/licenses/>
'''


import sys, os, subprocess
'''0
--------{GRN} codebase-autodoc {R0}-------- 
'''


'''4
{ULINE}Original Author{R0}: {BLUBG}midnqp{R0}
{ULINE}Initial Write{R0}  : Feb 21
{ULINE}License{R0}        : GPLv2
'''



def evaluate_colors(documentation):
	doc = documentation

	#colors
	COLORS = {
		# non-colors but important
		"__file__" : __file__,      # absolute name of this file
		"__argv0__" : sys.argv[0],  # relative name of this file


		"BLK": "\033[0;30m",
		"RED": "\033[0;31m",
		"GRN": "\033[0;32m",
		"YLW": "\033[0;33m",
		"BLU": "\033[0;34m",
		"CYN": "\033[0;36m",
		"WHT": "\033[0;37m",

		#background color: add 10 to the main color
		"BLKBG": "\033[0;40m",
		"REDBG": "\033[0;41m",
		"GRNBG": "\033[0;42m",
		"BLUBG": "\033[0;44m",
		"YLWBG": "\033[0;103m",
		"CYNBG": "\033[0;106m",

		#bright: add 30 to the main color
		"BCYN" : "\033[0;96m",

		#effects
		""   : "\033[0;0m",   # same as R0 - RESET all text effects
		"R0" : "\033[0;0m",
		"UL" : "\033[0;4m",   # same as underline
		"ULINE" : "\033[0;4m", 
	}

 
	colorNames = list(COLORS.keys())
	for i in range(len(colorNames)):
		repl = "{{{0}}}".format(colorNames[i])
		doc = doc.replace(repl, COLORS[colorNames[i]])
	return doc;




def self_document(filename, ts="  '''  ", te = "  '''  ", ts2 = "#", tabwidth=2):
	# default indentation of your source code is assumed: tabs


	f = filename
	ts = ts.strip()		#token start
	te = te.strip()		#token end
	c = open(f, "r").read().split("\n")		#corpora array, each line
	documentation = ''

	i=0
	while i < len(c):
		# c[i] is each line of the file, in array
		iot = c[i].find(ts)					#index of the token-start
		try:
			indent = int(c[i].strip()[len(ts) : ]) - (iot*tabwidth)
		except: 
			# No indent specified -- just ordinary programmers' commentry. Not part of the doc
			indent = -1 
		if iot >= 0 and indent != -1:
			j = i
			while j < len(c):
				# This loop documents anything after 
				# the nextline of token-start until 
				# beforeline of token-end.

				line = c[j+1].replace("\t", " "*tabwidth)
				if te in line: break
				else: 
					documentation += " "*indent
					documentation += line[iot*tabwidth : ]
					documentation += "\n"
				j+=1
		i+=1
	
	documentation = evaluate_colors(documentation)
	print(documentation, end="")




if __name__ == '__main__':
	try:
		filename = sys.argv[1]
		try: 
			# Trying for Usage 2
			ts = sys.argv[2]
			te = sys.argv[3]
			ts2 = sys.argv[4]
			self_document(filename, ts, te, ts2)
		except:
			# Usage 1
			self_document(filename)
	except:
		# No <filename> given
		self_document(__file__)
	'''0


	Usage:  python3  {__argv0__}  <filename>
	        python3  {__argv0__}  <filename>  [ts]  [te]  [ts2]
	'''

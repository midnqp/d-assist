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


#0 --------{GRN} codebase-autodoc {R0}-------- 
'''4
{UL}Original Author{R0}: {BLUBG}midnqp{R0}
{UL}Initial Write{R0}  : Feb 21
{UL}License{R0}        : GPLv2
'''



def evaluate_colors(documentation):
	doc = documentation
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
		""   : "\033[0;0m",  
		"R0" : "\033[0;0m",
		"UL" : "\033[0;4m", 
		"ULINE" : "\033[0;4m", 
	}

 
	colorNames = list(COLORS.keys())
	for i in range(len(colorNames)):
		repl = "{{{0}}}".format(colorNames[i])
		doc = doc.replace(repl, COLORS[colorNames[i]])
	return doc;




def document(ts, te, ts2):
	global documentation, i, iot, c  # using these already 'global'-declared global vars
	global tabwidth   # new variable for document() scope
	tabwidth = tw     

	error = False
	useTs = False
	useTs2 = False


	## ts2 :: Trying for single-line comments' token
	try: 
		ci = c[i]
		ciFwd = ci.index(ts2)+len(ts2)  #forward
		#isTs2 =  c[i][ciFwd - len(ts2): c[i].index(" ", ciFwd)].strip()
		indent = int(ci[ciFwd: ci.index(' ', ciFwd)])
		error = False
		useTs2 = True
	except : error = True


	## ts :: Trying for multi-line comments' token
	if error == True:
		try: 
			ci = c[i].strip()
			#print(f"Using Ts: {c[i]}  {int(c[i].strip()[len(ts):])}")
			indent = ci[len(ts) : ]
			isTs = ci[ci.index(ts) : ci.index(indent)]
			#print(f"isTs  ----------- <{isTs}>")
			if isTs == ts:
				#print(f"ts indent: -{indent}-  ={ci.strip()[:ci.index(indent)]}=")
				useTs= True
				error = False
		except Exception as e: 
			error = True

	
	if error == True: indent = -1

	

	if useTs == True and indent != -1:
		j = i
		while j < len(c):
			# This loop documents anything after 
			# the nextline of token-start until 
			# beforeline of token-end.
			line = c[j+1].replace("\t", " "*tabwidth)
			if te in line: break
			else: 
				documentation += " "*int(indent) 
				documentation += line[iot*tabwidth : ]
				documentation += "\n"
			j+=1
	elif useTs2 == True and indent !=-1:
		line = c[i].replace("\t", " "*tabwidth)
		documentation += " "*indent  
		lineForward = iot*tabwidth  + len(ts2) + len(str(indent)) + 1 
		documentation += line[lineForward: ]    
		documentation += "\n"






def self_document(filename, ts="  '''  ", te = "  '''  ", ts2 = "#", tabwidth=2):
	# CONSTRAINT \\\ Source code must be indented by tabs

	f = filename
	global c
	global documentation
	global iot
	global tw
	global i
	
	ts = ts.strip()		#token start
	ts2 = ts2.strip() #token start 2
	te = te.strip()		#token end
	tw = tabwidth
	documentation = ''
	c = open(f, "r").read().split("\n")		
	#corpora array of file, separated by newline

	i=0
	while i < len(c):
		# c[i] is each line of the file, in array
		iot = c[i].find(ts)					#index of the token-start
		if (iot >= 0): 
			document(ts, te, ts2)
		else:
			iot = c[i].find(ts2)
			if (iot >= 0): document(ts, te, ts2)
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

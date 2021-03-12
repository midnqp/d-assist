#!/usr/bin/python3

import sys, os, subprocess
import lib_avoidrepitition as L


'''0
d-assist: Execute frequently used commands abbreviatedly
Usage: d-assist    -option
       d-assist    -option    --arg    <value>

'''













'''0
AVAILABLE COMMANDS, OPTIONS, ARGUMENTS
``````````````````````````````````````
// Options: workspace
'''




def workspace_git():
	'''0
	-git    Pulls, adds, commits, pushes.
      --m     <str>  
							Commit message. Default: 
							"update at `date +'%y%m%d %H%M%S'`"
		  --p     <rebase|no-rebase|ff-only> 
							Specify type of pull.	Default: merge
		  --d     <dirpath> 
							Specify directory.
		  --v     <0|1> 
							Verbose. Default: 1
	'''
	
	m = L.arg(c, "--m", "`date +'%y%m%d %H%M%S'`")[0]
	p = L.arg(c, "--p", "")[0]
	if p != "": p = "--" + p.strip()
	d = L.arg(c, "--d", ".")[0]
	v = L.arg(c, "--v", "1")[0]
	

	#print(m, p, d)
	# processing inputs...	
	if int(v) == 0:	vt = "> /dev/null 2>&1"
	elif int(v) == 1: vt = ""
	workspaceGitCmd = ( 
			f'cd {d}; \
			git pull {p} {vt}; \
			git add -A; \
			git commit -m "{m}" {vt}; \
			git push {vt}'
	)
	
	#print(workspaceGitCmd)
	os.system(workspaceGitCmd)
	



def workspace_now():
	'''0
	-now    Displays current time
	'''
	os.system(f"date +'%y%m{L.GREENBG}%d %H%M{L.GREENBG}{L.R0} %S'")




def workspace_apt():
	'''
	-apt    Updates and upgrades Debian-based systems
	'''
	os.system("sudo apt-get update; sudo apt-get upgrade -y")




def workspace_dirs():
	'''0
	-dirs   Show sizes of directories
      --p     <dirpath>
							Specify directory path.
	'''
	# processing cmdline inputs...
	p = L.arg(cmdline, '--p', '.')[0]
	if p[-1] != '/':	p += '/'

	lslah = subprocess.getoutput(f'ls -lah {p}').split('\n')
	lslah = lslah[1:]
	ts = 0		# Total Size
	td = 0		# Total Dirs
	for i in range(len(lslah)):
		e = lslah[i]		# Each line in 'ls -lah'
		n = p + e[e.rindex(' ')+1 : ]	# The dirname or filename
		if e[0] == 'd' and n[-1] != '.' and n[-2:] != '..':
			td += 1
			dus = subprocess.getoutput(f"du -s {n}")
			duout= dus.split()[0]
			if duout.isdigit():
				ts += float(duout)
				print(subprocess.getoutput(f"du -sh {n}"))
	
	sMB = round(ts/1024, 2)		# Size in megabytes
	tsod = subprocess.getoutput("du -sh --exclude=/run/* --exclude=/proc/* "+p).split()[0]			# tsod = Total size of that directory

	print(f"\nTotal directories : {str(td)}")
	print(f"Total size of only directories: {str(sMB)} MB")
	print("Total size of {}: {}"
				.format('\033[0;30;106m' + p + L.R0, tsod)
	)




def workspace_launch():
	'''0
	-l      Launch programs abbreviatedly.
		  <x>     Launch xterm
		  <tx>    Launch a tabbed xterm
	'''
	def l_tx(): os.system("tabbed -c  xterm -into &")
	def l_x(): os.system("xterm &")

	launch = {
		"x"        : l_x,
		"tx"       : l_tx,
	}
	
	try: 
		l = sys.argv[2]
		launch[l]()
	except:	exit(errs[3])




def __help__():
	L.self_document(__file__)








AllOptions = {
	"--help" : __help__,

	"-git" : workspace_git,
	"-dirs": workspace_dirs,
	"-apt" : workspace_apt,
	"-now" : workspace_now,
	"-l"   : workspace_launch,
}




e = f"{L.RED}Error:{L.R0}"
errs = {
	1: f"{e} No -option specified.",
	2: f"{e} Argument required.",
	3: f"{e} Invalid argument/syntax.",

	404: f"{e} -option not found.",
}




try:
	cmdline = sys.argv[1:]
	c = cmdline
	option = cmdline[0]
except: 
	# The default fallback option
	# Updating the git repo.
	option="-git"


if option not in AllOptions: exit(errs[404])
elif option in AllOptions: AllOptions[option]()

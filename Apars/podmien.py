#!/usr/bin/env python

# uzycie: awk '{print $1}' nr | xargs -I {} ./podmien.py {}  # nr to plik z numerami aparow 
from sys import argv
f=open('otworz.html').read()		# czyta plik wzorcowy
f2=f.replace('104299610',argv[1])	# podmienia numer 
plik=open(argv[1],'w')
print >> plik, f2
plik.close()



#!/usr/bin/env python

# uzycie: awk '{print $1}' nr | xargs -I {} ./podmien.py {}  # nr to plik z numerami aparow 
# from sys import argv
# f=open('otworz.html').read()		# czyta plik wzorcowy
# f2=f.replace('104299610',argv[1])	# podmienia numer
# plik=open(argv[1],'w')
# print >> plik, f2
# plik.close()
#
#

# import os
# import shutil
# from sys import argv
#
# f=open('template.html').read()
# f1=open('nr.txt', 'r')
#
# newpath='selenium/'
# for i in f1:
#     if not os.path.exists(newpath):
#         os.makedirs(newpath)
#     f2=f.replace('104299610',i)
#     file_for_selenium=open(i,'w')
#     file_for_selenium.write(f2)
#     file_for_selenium.close()
#     shutil.move(i, newpath+i)


import os
import shutil
import sys


arg=sys.argv[1]


f=open('template.html').read()
f1=open(arg , 'r')

newpath='selenium1/'
for i in f1:
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    f2=f.replace('104299610',i)
    file_for_selenium=open(i,'w')
    file_for_selenium.write(f2)
    file_for_selenium.close()
    shutil.move(i, newpath+i)






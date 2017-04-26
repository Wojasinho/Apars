# import wget
import urllib2
import sys
import os
import shutil
sys.path.append(('/home/wojasinho/Project/apars/Apars/'))


# url = 'https://advisories.secintel.ibm.com/adv_database.php?adv_id=67667'
# # url='http://www.wp.pl'
# # filename = wget.download(url)
# # filename
# # print filename
#
#
# response = urllib2.urlopen(url,)
# content = response.read()
# f = open( "adv_database.php?adv_id=6", 'w' )
# f.write( content )
# f.close()
import os
import  codecs

nr = open('nr.txt','r',)
advlist=open('advlist.txt', 'r')
newpath = 'apar_to_analyse/'

for number in nr:
    advline=advlist.readline()
    number=number.rstrip()

    if len(advline) == 0:
        break

    if not os.path.exists(newpath):
        os.makedirs(newpath)
    adv = open(number, 'w')

    response = urllib2.urlopen(advline, )
    content = response.read()

    adv.write(content)
    adv.close()
    shutil.move(number, newpath + number)


# template = open('template.html').read()
#
# fileapar = open('nr.txt', 'r')
# newpath = 'selenium/'
#
# for number in fileapar:
#     if len(number) == 0:
#         break
#     if not os.path.exists(newpath):
#         os.makedirs(newpath)
#
#     if number == '\n'  :
#         continue
#
#     tempvar = template.replace('123456789', number)
#     nrapar = open(number, 'w')
#     nrapar.write(tempvar)
#     nrapar.close()
#     shutil.move(number, newpath + number)
# import wget
import urllib2
import sys
import os
import shutil
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
sys.path.append(('/home/wojasinho/Project/apars/Apars/'))

advlist=open('advlist.txt', 'r')
newpath = 'adv/'
for url in advlist:
    i=url
    i.rstrip(os.linesep)
    if len(url) == 0:
        break
    if not os.path.exists(url):
        os.makedirs(url)
    url.strip('\r\n')
    response = urllib2.urlopen(url, )
    content = response.read()
    adv = open(url, 'w')
    adv.write(content)
    adv.close()
    # shutil.move(url, newpath + url)

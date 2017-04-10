# Script which can pattern available package on server.
# Requirement enviroment Python 3.6.1

import re
import sys
import pprint

Arch='x86_64'

product_interest = (
    'Red Hat Enterprise Linux',
    'Red Hat Enterprise Linux (v. 5 server)',
    'Red Hat Enterprise Linux Server (v. 6)',
    'Red Hat Enterprise Linux Server (v. 7)',
)

product_not_interest = (
    'Oracle Java for Red Hat Enterprise Linux',
    'Red Hat Enterprise Linux Supplementary',
    'Red Hat Enterprise Linux Server Supplementary (v. 6)',
    'Red Hat Enterprise Linux Server Supplementary (v. 7)',
)


sys.path.append(('/home/Wojasinho/Programming/Apars/apars/Apars/'))

# print(sys.path)

f = open('adv_database.php?adv_id=65438')
print (f.readline())

print (f)
# print (f)


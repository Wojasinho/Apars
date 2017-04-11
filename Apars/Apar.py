# Script which can pattern available package on server.
# Requirement enviroment Python 3.6.1

import re
import sys
import pprint

# Defined architecture
Arch='x86_64'

# Definded interested names of Product  (Mostly it should be RHEL Servers v. X)
product_interest = (
    'Red Hat Enterprise Linux',
    'Red Hat Enterprise Linux (v. 5 server)',
    'Red Hat Enterprise Linux Server (v. 6)',
    'Red Hat Enterprise Linux Server (v. 7)',
)

# Definded not interested names of Product, which we can skip
product_not_interest = (
    'Oracle Java for Red Hat Enterprise Linux',
    'Red Hat Enterprise Linux Supplementary',
    'Red Hat Enterprise Linux Server Supplementary (v. 6)',
    'Red Hat Enterprise Linux Server Supplementary (v. 7)',
)
#Append paths for Files with APARS
sys.path.append(('/home/Wojasinho/Programming/Apars/apars/Apars/'))
sys.path.append(('/home/wojasinho/Projects/apars/Apars/'))

# print(sys.path)

file = open('adv_database.php?adv_id=65438')

while True:

    line=file.readline()
    line=file.lstrip()
    True


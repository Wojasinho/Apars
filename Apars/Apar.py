# Script which can pattern available packages on server (APARS == patch package supported by RHEL)
# Requirement enviroment for script Python 3.6.1

import re
import sys
import pprint

# Defined architecture
Arch='x86_64'

# Definded interested names of Product  (Mostly it should be RHEL Servers v. X)
product_interest = [
    'Red Hat Enterprise Linux',
    'Red Hat Enterprise Linux (v. 5 server)',
    'Red Hat Enterprise Linux Server (v. 6)',
    'Red Hat Enterprise Linux Server (v. 7)',
    'Red Hat Enterprise Linux Desktop (v. 6)',
]
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
    line = file.readline()
    line = line.lstrip()

    # Skip white line
    if len(line)==0 :
        continue

    # Find on raw text 'Synopsis' (concept of patch)
    if line[0:8]=='Synopsis':
        Synopsis = line

        continue

    # Find on raw text 'Advisory ID' (ex. RHSA-2016:0760-01)
    if 'Advisory ID:       ' in line:
        Advisory_ID=line


        continue

    # Find on raw text interest Product (ex.Product    : Red Hat Enterprise Linux)
    if 'Product:       ' in line:
        Product=line.split(':')[1].lstrip()

        continue

    # Find on raw text date
    if 'Issue date       :' in line:
        date=line
        continue

    if 'Package List:' in line:
        Package=line
        while True:
            line = file.readline()
            line = line.lstrip()

            if len(line) == 0:
                continue
        # It should be works with loop
            if any(product_interest in line):

                candidate = line


    else:
        continue




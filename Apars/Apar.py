# Script which can pattern available packages on server (APARS == patch package supported by RHEL)
# Requirement enviroment for script Python 3.6.1

import re
from sys import argv
import pprint


# Defined architecture
arch = 'x86_64'

# List of candidate
candidate = {}
products = []


# Defined interested names of Product  (Mostly it should be RHEL Servers v. X)
products_interest = (
    'Red Hat Enterprise Linux Workstation Optional (v. 6)',
    'Red Hat Enterprise Linux Workstation (v. 6)',
)
# Defined not interested names of Product, which we can skip
products_not_interest = (
    'Oracle Java for Red Hat Enterprise Linux',
    'Red Hat Enterprise Linux Supplementary',
    'Red Hat Enterprise Linux Server Supplementary (v. 6)',
    'Red Hat Enterprise Linux Server Supplementary (v. 7)',
)
# Append paths for Files with APARS
sys.path.append(('/home/Wojasinho/Programming/Apars/apars/Apars/'))
sys.path.append(('/home/wojasinho/Projects/apars/Apars/'))

# print(sys.path)

# Defined char which, you can skip in line
bad = ('@', '<', '!', '#', '{', '}', ',', '.', ';', ':')



for apar in argv[1:]:

    file = open(apar)
    while True:
        line = file.readline()
        line = line.lstrip()

        # Skip white line
        if len(line) == 0:
            continue
        # Skip first 'bad' char in line :
        if line[0] in bad:
            continue

        # Find on raw text 'Synopsis' (concept of patch)
        if line[0:8] == 'Synopsis':
            Synopsis = line

            continue

        # Find on raw text 'Advisory ID' (ex. RHSA-2016:0760-01)
        if 'Advisory ID:       ' in line:
            Advisory_ID = line

            continue

        # Find on raw text interest Product (ex.Product    : Red Hat Enterprise Linux)
        if 'Product:       ' in line:
            Product = line.split(':')[1].lstrip()

            continue

        # Find on raw text date
        if 'Issue date       :' in line:
            date = line
            continue

        if 'Package List:' in line:
            Package = line
            break

    while True:

        # Var for next loop 'while'
        trigger = True

        # Format lines (strip method for whitespace from left side and colon from right side)
        line = file.readline()
        line = line.lstrip().rstrip(':\n')

        # # Skip white line
        if len(line) == 0:
            continue
        # Skip first 'bad' char in line :
        if line[0] in bad:
            continue

        if line in products_interest:
            print(line)
            products.append(line)

            while trigger:
                line = file.readline()
                line = line.lstrip().rstrip(':\n')

                if "Source" in line:
                    continue

                if arch in line:

                    while len(line) > 0:

                        line = file.readline()
                        line = line.lstrip()

                        if len(line) == 0:
                             trigger= False
                             break

                        if line.split('.')[-2] == arch:
                            line = line.lstrip().rstrip(':\n')
                            print(line)


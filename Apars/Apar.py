# Script which can pattern available packages on server (APARS == patch package supported by RHEL)
# Requirement enviroment for script Python 2.6.6

import re
import pprint
import os
import shutil
import sys
import wget






class Apar(object):
    def __init__(self):
        # Append paths for Files with APARS
        sys.path.append(('/home/Wojasinho/Programming/apars/Apars/'))
        sys.path.append(('/home/wojasinho/Project/apars/Apars/'))

        # Number of interested APARS in txt file
        self.arg = sys.argv[1]
        self.arg2= sys.argv[2]

        # Defined architecture
        self.arch = 'x86_64'


    def genereteFile(self):
        # Aim of these function is  generate n files which can we upload to Selenium
        # Selenium can open automatically our source code and can give us row description of Apar
        # which we can analyse in next step. We have to repeat these process with n Apars, so we
        # have to generate  file for each Apars number

        # Template from Selenium
        # These template.html can open automatically in Cirats our Apar, we have to
        template = open('template.html').read()

        fileapar = open(self.arg, 'r')
        newpath = 'selenium/'

        for number in fileapar :
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            tempvar = template.replace('103880775',number)
            nrapar = open(number,'w')
            nrapar.write(tempvar)
            nrapar.close()
            shutil.move(number, newpath+number)


    def analyse(self):

        advlist = open(self.arg2, 'r')
        # advlist = open('advlist.txt','r')



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

        # sys.path.append(('/home/wojasinho/Projects/apars/Apars/'))

        # print(sys.path)

        # Defined char which, you can skip in line
        bad = ('@', '<', '!', '#', '{', '}', ',', '.', ';', ':',)

        # Defined path where you located row apars


        for i in advlist:

            # Loop for each apar in directory
            # path = '/home/Wojasinho/Programming/apars/adv/' +
            path = '/home/wojasinho/Projects/apars/Apars/'
            print("Now we are analysing " + i)
            i=i.rstrip('\n')
            self.apars = open(i,'r')
            # file = open('/home/Wojasinho/Programming/apars/adv/adv_database.php?adv_id=65438')

            while True:

                line = self.apars.readline()
                line = line.lstrip()

                # Skip white line
                if len(line) == 0:
                    continue
                # Skip first 'bad' char in line :
                if line[0] in bad:
                    continue

                # Find on raw text 'Synopsis' (concept of patch)
                if line[0:8] == 'Synopsis':
                    line = line.rstrip('\n')
                    Synopsis = line

                    print(Synopsis)
                    continue

                # Find on raw text 'Advisory ID' (ex. RHSA-2016:0760-01)
                if 'Advisory ID:       ' in line:
                    Advisory_ID = line
                    print(Advisory_ID)
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

                if "7. References" in line:
                    break
                # Var for next loop 'while'
                trigger = True

                # Format lines (strip method for whitespace from left side and colon from right side)
                line = self.apars.readline()
                line = line.lstrip().rstrip(':\r\n')

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
                        line = self.apars.readline()
                        line = line.lstrip().rstrip(':\r\n')

                        if "Source" in line:
                            continue

                        if self.arch in line:

                            while len(line) > 0:

                                line = self.apars.readline()
                                line = line.lstrip()

                                if len(line) == 0:
                                    trigger = False
                                    break

                                if line.split('.')[-2] == self.arch:
                                    line = line.lstrip().rstrip(':\r\n')
                                    print(line)
            print("\n")
            print("Analyse process of " + i + " has been finshed \n\n")


#
# test = Apar()
# test.genereteFile()
# test.analyse()


url = 'http://www.onet.pl.com'
filename=wget.download(url)
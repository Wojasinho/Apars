# Script which can pattern available packages on server (APARS == patch package supported by RHEL)
# Requirement enviroment for script Python 2.6.6

import os
import shutil
import sys
import urllib2


class Apar(object):

    def __init__(self):
        # Append paths for Files with APARS
        sys.path.append(('/home/Wojasinho/Programming/apars/'))
        sys.path.append(('/home/wojasinho/Project/apars/Apars/'))
        sys.path.append(('/home/wojasinho/Project/apars/Apars/apar_to_analyse/'))

        # Number of interested APARS in txt file
        # self.arg = sys.argv[1]
        # self.arg2= sys.argv[2]

        self.arg = open('nr.txt', 'r')
        self.arg2 = open('advlist.txt', 'r')

        self.newpath = 'apar_to_analyse/'
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
        newpath = 'apar_to_selenium/'

        for number in fileapar:

            if len(number) == 0:
                break

            if number == '\n':
                continue

            if not os.path.exists(newpath):
                os.makedirs(newpath)

            tempvar = template.replace('123456789', number)
            number=number.rstrip()
            nrapar = open(number, 'w')
            nrapar.write(tempvar)
            nrapar.close()
            shutil.move(number, newpath + number)

    def download(self):

        nr = open(self.arg, 'r')
        advlist = open(self.arg2, 'r')

        for number in nr:

            advline = advlist.readline()

            number = number.rstrip()

            if len(advline) == 0:
                    break

            if not os.path.exists(self.newpath):
                os.makedirs(self.newpath)

            adv = open(number , 'w')

            response = urllib2.urlopen(advline,)
            content = response.read()

            adv.write(content)
            adv.close()
            shutil.move(number , self.newpath + number)

    def analyse(self):

        nr= self.arg


        # List of candidate
        candidate = {}
        products = []
        package=[]

        # Defined interested names of Product  (Mostly it should be RHEL Servers v. X)
        products_interest = (
            'Red Hat Enterprise Linux Server (v. 4)',
            'Red Hat Enterprise Linux Server (v. 5)',
            'Red Hat Enterprise Linux Server (v. 6)',
            'Red Hat Enterprise Linux Server (v. 7)',
            'Oracle Java for Red Hat Enterprise Linux',
            'Red Hat Enterprise Linux Supplementary',
            'Red Hat Enterprise Linux Server Supplementary (v. 6)',
            'Red Hat Enterprise Linux Server Supplementary (v. 7)',
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


        for self.number in nr:
            print("*******************************************************************")

            checker = []
            products=[]



            # Loop for each apar in directory
            start=("Now we are analysing " + self.number)
            self.number = self.number.rstrip('\n')
            self.apars = open(self.newpath+self.number, 'r')


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
                    self.Synopsis = line

                    # print(Synopsis)
                    continue

                # Find on raw text 'Advisory ID' (ex. RHSA-2016:0760-01)
                if 'Advisory ID:       ' in line:
                    self.Advisory_ID = line
                    # print(Advisory_ID)
                    continue

                # Find on raw text interest Product (ex.Product    : Red Hat Enterprise Linux)
                if 'Product:       ' in line:
                    Product = line.split(':')[1].lstrip()

                    continue

                # Find on raw text date
                if 'Issue date       :' in line:
                    self.date = line
                    continue

                if 'Package List:' in line:
                    Package = line
                    break

            while True:

                if "7. References" in line:

                    if len(checker) > 0:
                        out=("Apar : " + self.number +" "+ "is applicable ")
                        # output = open("output.txt", 'w')
                        # output.write(out)
                        # output.close()
                        print (start)
                        print (self.Synopsis)
                        print (self.Advisory_ID)
                        # print (date)
                        # print (finish)
                        for output in products:
                            print (output)
                    else:
                        print("Apar : " + self.number +" "+ "is not applicable")

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

                    temp=line
                    checker.append(line)
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
                                    products.append(line)
                                    # package=package.append(line)
                                    # candidate[temp]=package
                                    # print (line)
                                    # print(self.number)
            finish = ("Analyse process of " + self.number + " has been finshed \n\n")

    def applicable(self):
        pass


#
test = Apar()
# test.genereteFile()
# test.download()
test.analyse()

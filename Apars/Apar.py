"""
Script which can pattern available packages on server (APARS == patch package supported by RHEL) for dedicated products
and architecture.

Requirement enviroment for script Python 2.6.6
Requirement access : Cirats

Author: Wojciech Koszela
Contact: WKoszela@pl.ibm.com
Company: IBM POLAND



Instruction :


It looks like a lot of steps, don't worry it's really fast. You will save couple of time.

1.  Create enviroment :
        1.1.    Create directory and copy there "Apar.py
        1.2.    Write your number of Apars to file nr.txt in directory
        1.3.    Add your directory to Apar.py (sys.path.append('path') -> line 46
         
2.  Generete files and apply to Selenium
        2.1.    330,331 lines - commented,  329 line uncommented
        2.2.    execute from terminal: python Apar.py
3.  Log in to Cirats / apply to Selenium your files with "s" at the end of name("nr_apar_s) and run Selenium
4.  Go to Mozilla Firefox -> Ctrl+Shift+h , tab "Today", filter by name, select and copy your last address to new file 
        advlist.txt - addresses started from  ( ex.https://advisories.secintel.ibm.com/adv_database.php?adv_id=70267).
5.  Download row source Apars
        5.1.    329,331 lines - commented,  330 line uncommented
        5.2.    It's longest operation in these procedure, depends of network connection, server status etc.
        5.3     from bash terminal : python Apar.py
6.  Analyse output
        6.1     329,330 lines - commented,  331 line uncommented
        6.2     Forward output to txt file
        6.3     execute from terminal: python Apar.py > output.txt
    

"""

import os
import shutil
import sys
import urllib2


class Apar(object):

    def __init__(self):

        # Append your local paths for script files
        sys.path.append(('/home/wojasinho/Project/apars/Apars/'))

        # sys.path.append(('/home/wojasinho/Project/apars/Apars/apar_to_analyse/'))

        # Number of interested APARS in txt file (argument)
        # self.arg = sys.argv[1]

        # List of interested link in txt file (argument)
        # self.arg2= sys.argv[2]

        self.arg = open('nr.txt', 'r')
        self.arg2 = open('advlist.txt', 'r')

        self.newpath = 'apar_to_analyse/'

        # Defined interested architecture (noarch, x86_64, ppc64le, ppc64, s390x,)
        self.arch = 'x86_64'

    def genereteFile(self):

        """
        Aim of these method is to  generate n files which can we upload to Selenium (plugin in Mozilla Firefox)
        Selenium can open automatically our source code which we generete below and can give us row description of Apar
        which we can download and analyse in next step ( method download(), analyse(). We have to repeat these process
        with n Apars, so we have to generate  file for each Apar number
        """




        # Template from Selenium

        # These template.html can open automatically in Cirats our Apar, we have to generete n files (such as
        # template.html) with changed apar number inside in code, then we can apply these file to Selenium, which can
        # open n pages on Firefox.

        template = open('template.html').read()

        fileapar = self.arg

        newpath = 'apar_to_selenium/'

        # Loop which replace number Apar from file nr.txt and write each separete file to directory - 'apar_to_selenium/'



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
            shutil.move(number, newpath + number+"s")

    def download(self):
        """
        
        Aim of these method is to download source code of each apar's website. The download() method save it in
        directory 'apar_to_analyse'. It's a longest operation of these Class. We need to pass to run these method, two
        arguments (nr.txt - list of apar's number, advlist.txt - list of links (from history Mozilla Firefox, which
        was opened by Selenium (in previous method we genereted file which were uploaded to Selenium). Now we need output
        from history and paste to advlist.txt
        
        """



        nr = self.arg
        advlist = self.arg2

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
        """
        
        Aim of these method is to analyse row source of each apars in format html. We can defined interested architecture
        and products(solution). These method analyse html each apar seperate . Script can find Advisory_ID, Product,
        Issue date, and dedicated package for architecture and product.
        
        """
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
                        print (start)
                        print (self.Synopsis)
                        print (self.Advisory_ID)
                        # print (date)
                        # print (finish)
                        for output in products:
                            print (output)
                        print (out)
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



#Construct new instance
apar = Apar()

# Create new method - run script only with one method
# apar.genereteFile()
# apar.download()
apar.analyse()

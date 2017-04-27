v.1.0 
Apars

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
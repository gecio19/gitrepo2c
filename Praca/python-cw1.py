#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  python-cw1.py
#  
#  Copyright 2018  <>
#  

#  
#  



    


def main(args):

    a = int(input("Podaj 1. liczbę: ")) 
    
    
        
    while a < 75:   #Pętla pobiera cyfrę a i sprawdza czy jest mniejsza od 75 jeżeli jest mniejsza pobiera kolejną cyfre (b) i dodaję ją do a i powtarza funckję do czasu gdy a będzie większe od 75
	
        
        b = int(input("Podaj 2. liczbę: ")) 
        a = a + b
        
   
         
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

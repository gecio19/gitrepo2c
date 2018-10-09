#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pusty prostokat.py
def prostokat(a, b, znak):
    for i in range(a):
        for j in range(b):
            print(znak, end='')
        print()
        
        
def prostokat2(a, b, znak, znak2):
    for i in range(a):
        for j in range(b):
            if j == 0 or i == 0:
                print(znak  , end='')
            else:
                print(znak2 * b, end='')
        print()
        
        

        

def main(args):
    
    a = int(input("Podaj pierwszy wymiar:"))
    b = int(input("Podaj drugi wymiar:"))
    znak = (input("Podaj pierwszy znak:"))
    znak2 = (input("Podaj drugi znak:"))
    
    b = b - 1
    
    prostokat(a, b, znak)
    print(" ")  
    prostokat2(a, b, znak, znak2)
    
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  szablon.py
#  int()- przekształca argument na liczbę całkowtią czyli typ INTEGER(Liczba całkowita)
#DRY - don't repeat yourself

def hello():
    print("Witaj, jestem Python")
    
    
def witaj():
   print("Witaj") 
   c = input("Podaj swoje imię? ")
   print ("Witaj", c ) 



def suma(l1, l2):
    #print("suma", l1 + l2 )
    suma(a, b)

def różnica(l1, l2):
    print ("różnica", l1 - l2 ) 
    różnica(a, b)  
def iloraz (l1, l2):
    print ("iloraz", l1 * l2 )
    iloraz (a, b)
def iloczyn (l1, l2):         
    iloczyn (a, b) 
    
def main(args):
    
    witaj()
    a = int(input("Podaj 1. liczbę: ")) 
    b = int(input ("Podaj 2. liczbę: "))
    
    print(a) 
    print (b)
    
    
    print ("Suma:", a + b)
    print ("Różnica:", a - b)
    print ("Iloczyn:", a * b)
    print ("Iloraz:", a / b)
    hello() #wywołanie funkcji
    
    
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

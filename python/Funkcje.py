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
    print("suma", l1 + l2 )
    
def suma2(a, b):

    """
    Funkcja sumuje dwie liczby i zwraca wynik
    """
    return a + b    
    

def roznica(l1, l2):
    print ("różnica", l1 - l2 ) 
     
def iloraz (l1, l2):
    print ("iloraz", l1 * l2 )
    
def iloczyn (l1, l2):         
     print ("iloczyn", l1 / l2 )
    
def main(args):
    #Zmienne lokalne, o zasięgu lokalnym
    witaj()
    a = int(input("Podaj 1. liczbę: ")) 
    b = int(input ("Podaj 2. liczbę: "))
    
    print(a) 
    print (b)
    
    
    print ("Suma:", suma2(a, b))
    #print ("Różnica:", a - b)
    roznica(a, b)
    #print ("Iloczyn:", a * b)
    iloczyn(a, b)
    #print ("Iloraz:", a / b)
    iloraz(a, b)
    hello() #wywołanie funkcji
    
    
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

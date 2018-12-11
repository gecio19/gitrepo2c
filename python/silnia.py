#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.html

#Oczliczanie potegi podstawy podniesionej do wykładnika.

def silnia_re(n):
    if n == 0:
        return 1 
    return silnia_re(n-1) * n    



def silnia_it(n):
    #0! =1 
    #<1;n> n! = 1 *... * n dla <1;n>
    wynik = 1
    for i in range(1, n + 1):
        
        
        wynik = wynik * i
        print(wynik)
    return wynik
    
    



def main(args):
    n = int(input("Podaj 1. liczbę: "))
    #n = int(input("Podaj liczbe "))
    #print("{}! = {} ". format(n, silnia_it(n)))
    
    assert(silnia_it(4) == 24)
    assert(silnia_it(10) == 3628800) 
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

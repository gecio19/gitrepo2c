#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.html

#Oczliczanie potegi podstawy podniesionej do wykładnika.

def potega_it(a, n):
    wynik = 1
    for i in range(n):
        
        
        wynik = wynik * a
        #print(wynik)
    return wynik
    
    



def main(args):
    #a = int(input("pdodaj podstawe:"))
    #n = int(input("pdodaj podstawe:"))
    #print("Potega {} do {} wynosi {}". format(a, n, potega_it(a, n)))
    assert(potega_it(1, 1) == 1)
    assert(potega_it(2, 10) == 1024)
    assert(potega_it(1, 0) == 1)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

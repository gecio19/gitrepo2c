#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby23.py


def liczby2():
    """
    Funkcja drukuje wszystkie liczby 2- crfrowe, w którch nie powatrzają się cyfry. 
    Na koniec zwraca ilośc takich liczb.
    Wykluczone liczby: 11,,22,33 itd.
    
    """
    
    
    licznik = 0
    for i in range(1, 10): # Pętla dziesiątek
        for j in range(10):# Petla jedności
            if j != i:                                   #"!=" oznacza jest rózna
                print("{}{} ".format(i, j), end="")
                licznik = licznik + 1 #zliczanie liczb
    return licznik



def liczby3():
    """
    Funkcja drukuje wszystkie liczby 2- crfrowe, w którch nie powatrzają się cyfry. 
    Na koniec zwraca ilośc takich liczb.
    Wykluczone liczby: 11,,22,33 itd.
    
    """
    
    
    licznik = 0
    for i in range(1, 10):        # Pętla dziesiątek
        for j in range(10):          # Petla jedności
            for k in range(10):
                if i != j != k != i:                                   #"!=" oznacza jest rózna
                    print("{}{}{} ".format(i, j, k), end=" ")
                    licznik = licznik + 1 #zliczanie liczb
    return licznik







def main(args):
    
    
     print("\n\nliczczb 2-cyfrowych:", liczby2())
     print(" ")
     print("\n\nliczczb 3-cyfrowych:", liczby3())
    
    
    
    
    
    
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

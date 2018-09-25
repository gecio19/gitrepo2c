#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla-for.py
#  



def main(args):
    
    start = int(input("Podaj 1. liczbę: ")) 
    stop = int(input("Podaj 2. liczbę: ")) 
    
    while start >= stop: #Jeżeli start jest większy od stop pwowiedz "Bład" i pobierz ponownie drugą liczbę do skutku s
      print("Błąd")
      stop = int(input("Podaj 2. liczbę: ")) 
  
      
    
    if start>= stop: #Bierze liczbę1 podaną  
        print("Błędnę dane!")
        exit(0)
    for i in range(start, stop + 1):
        if i % 2 == 0: # Jeżeli liczba i jest parzysta drukuję ją 
            print(i)
        else:
            print("Liczba nieparzysta")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

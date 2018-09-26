#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla-for.py
#  



def main(args):
    
    start = int(input("Podaj 1. liczbę: ")) 
    stop = int(input("Podaj 1. liczbę: ")) 
    
    if start>= stop:
        print("Błędnę dane!")
        exit(0)
    for i in range(start, stop = 100):
        if i % 2 == 0:
            print(i)
        else:
            print("Liczba nieparzysta")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

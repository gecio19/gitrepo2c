#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  spr.py
#  
#  Copyright 2018  <>





def main(args):
    n = int(input("Podaj liczbe:"))
    i = 2;
    while i * i <= n:
        if n % i == 0:
            print("Zlozone")
            return 0
         i += 1       
        print("Pierwsza")
        return 0
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

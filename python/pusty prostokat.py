#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pusty prostokat.py



def main(args):
    
    m = int(input("Podaj pierwszy wymiar:"))
    n = int(input("Podaj drugi wymiar:"))
    z = (input("Podaj pierwszy wymiar:"))
    for i in range(m):
        for j in range(n):
            print(z, end='')
        print()
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

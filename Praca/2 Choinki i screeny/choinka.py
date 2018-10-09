#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  choinka.py




def choinka(a, znak):
    for i in range(a):
        for j in range(a):
            if j == 0 :
                print(i * znak, end='')
        print()




def main(args):

    a = int(input("Podaj wysokośc h:"))
    znak = (input("Podaj pierwszy znak:"))
   
    
    choinka(a, znak)	
	
	
	
	
	
	
	
	
	
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

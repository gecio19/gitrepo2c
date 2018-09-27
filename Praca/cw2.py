#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cw2.py
#  
#  
#  


def main(args):
	
	
	
	
	
	n = int(input("Podaj liczbę  naturalną "))   #Program pobiera cyfrę n
	if n < 0:                               #Sprawdza czy jest ona naturalna jeżeli nie powiadami o tym i wyłącza program     
		print("Liczba nie jest naturalna")
		return 0
	m = int(input("Podaj kolejną liczbę naturalną  ")) 	   #Program pobiera cyfrę m
	if m < 0:                                       #Sprawdza czy jest ona naturalna jeżeli nie powiadami o tym i wyłącza program
		print("Liczba nie jest naturalna")                
		return 0
	
	
	
	
	
	
	for i in range(n, m):         # Funckcja pobiera zmienne n i m ustawia je jako pierwszą i drugą cyfrę zbioru i wyposuje je 
	
		print (i, "")
	
	
	
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

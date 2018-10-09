#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cw2.py
#  
#  
#  


def main(args):
	
	
	
	
	
	n = int(input("Podaj liczbę  naturalną "))   #Program pobiera cyfrę n
	while n < 0:                               #Sprawdza czy jest ona naturalna jeżeli nie powiadami o tym i powtórzy     
		print("Liczba nie jest naturalna")
		n = int(input("Podaj liczbę  naturalną "))
	m = int(input("Podaj kolejną liczbę naturalną  ")) 	   #Program pobiera cyfrę m
	while m < n:                                       #Sprawdza czy jest ona naturalna jeżeli nie powiadami o tym i powtórzy
		print("Liczba nie jest naturalna")                
		m = int(input("Podaj liczbę  naturalną "))
	
	
	
	
	
	
	for i in range(n, m + 1):         # Funckcja pobiera zmienne n i m ustawia je jako pierwszą i drugą cyfrę zbioru i wyposuje je 
	
		print (i," ", end =" ")
	
	
	
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

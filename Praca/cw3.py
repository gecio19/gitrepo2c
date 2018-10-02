#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cw3.py
#  
#  


def main(args):
	
	
	
	m = int(input("Podaj liczbę która bedzie kończyłą przedział  ")) 	   #Program pobiera cyfrę m
	while m < 0:                                       #Sprawdza czy jest ona naturalna jeżeli nie powiadami o tym i powtarza się 
		print("Liczba nie jest naturalna")                
		m = int(input("Podaj liczbę która bedzie kończyłą przedział  ")) 	   
	
	
	
	
	
	
	for i in range(0, m + 1):         # Funckcja pobiera zmienna m i drukuję listę w przedziale od 0 do m 
	
		print (i*i," ", end = " ")             #Dzięki tej funkcji cyfry są drukowane   do kwadracie 
	
	

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
                                                                    

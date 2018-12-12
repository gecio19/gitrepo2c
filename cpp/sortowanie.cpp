/*
 * sortowanie.cpp
 * 
 * Copyright 2018  <>
 * 

 */
using namespace std;


#include <iostream>
#include <cstdlib>

void wypelnij(int tab[], int roz) {
    srand(time(NULL)); 
    
    cout << "Wprowadź rozmiar" << roz << "liczb: " << endl;
    for(int i=0; i<roz; i++) {
        tab[i] = rand() % 101; // liczby od 0 do 100
        
        } 
    
}

void drukuj(int tab[], int roz) {
    for(int i=0; i<roz; i++) {
        cout << tab[i] << " " << endl;
        
        } 
    
}


int main(int argc, char **argv)
{
    
    
	
	return 0;
}


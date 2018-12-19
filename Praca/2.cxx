/*
 * 2.cxx
 * 
 * Copyright 2018  <>
 
 * 
 */


using namespace std;


#include <iostream>


int main(int argc, char **argv)
{
    int n = 6;
    int szuk = 5;
    int i = 0;
    int tab[n + 1] = {1,4,6,2,9,5};
    tab[n] = szuk;
    
    while (tab[i] != szuk) i++;
    
    if (i < n)
        cout << "Znaleziony";
    else
        cout << "Nie znaleziony";
    return 0;
    
	
	return 0;
}


/*
 * spr.cxx
 * 
 * Copyright 2018  <>
 * 

 * 
 */


#include <iostream>
using namespace std;


int main(int argc, char **argv)
{
    
    int n = 0;
    cout << "Podaj liczbe";
    cin >> n;
    int i =2;
    for(i = 2; i*i <= n; i++) {
        
        
        
        
        if(n % i == 0)  {
            
            cout << "liczba złożona";
            return 0;
            
            }
        
        
        }
    
    
	cout << "Liczba pierwsza";
	return 0;
}


/*
 * potega.cxx
 * 
 * Copyright 2018  <>
 
 */


#include <iostream>
using namespace std;

int  potega_it(int a, int n){
    int wynik = 1;
    for(int i = 0; i < n; i++)
     {
        
        wynik = wynik * a;
        
        
        }
        return wynik;
    
    
}
    
int potega_re(int a, int n)
    {
        if (n== 0) return 1;
        return potega_re(a, n-1) * a;
            
    
    
    
    }    



int main(int argc, char **argv)
{
    int a, n;
    cout << "Podaj podstawe i wykładnik";
    cin >> a >> n;
    cout << "potega:" << potega_it(a, n) << endl;
    cout << "potega:" << potega_re(a, n) << endl;
	
	return 0;
}


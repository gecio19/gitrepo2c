/*
 * Fobonacci.cxx
 * 
 * Copyright 2018  <>

 */
 
 
 


#include <iostream>

using namespace std;

long int fibonacci_re(int n)
{
    if(n == 0){
        return 0;
    }
    else(n == 1)
    
        return 1;
      
    return fibonacci_re(n);
}
long int fibonacci_it(int n){
    
    long int wynik = 0; 
    
    
    long int a = 0; // n - 2
    long int b = 1; // ryraz n - 1
    
    
    
    if(n == 0) return a;
    if(n == 1) return b;
    for(int i = 2; i <= n; i++) {
        
        wynik = a + b;
        a = b;
        b = wynik;

        
        
        
        
        
        }
      
        
    
    
    
    return wynik;
    
    }






int main(int argc, char **argv)
{
    
    int n;
    cout << "Podaj numer wyrazu ciągu";
    cin >> n;
    
    cout << "Ciąg fibonacciego do wyrazu" << n << ":" << endl;
    
    
    
    
    // instrukcja które wydrkuje wszystkie poprzednie ciągi 
    cout << fibonacci_it(n);
    cout << fibonacci_re(n);
    
    
    
    
    
    
	
	return 0;
}


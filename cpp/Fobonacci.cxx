/*
 * Fobonacci.cxx
 * 
 * Copyright 2018  <>

 */
 
 
 


#include <iostream>

using namespace std;

long int fibonacci_re(int n)
{
    if (n== 0) return 0;
    if (n== 1) return 1;
    return fibonacci_re(n-1) + fibonacci_re(n-2);

    
    
    
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
    
    
    
    
    for(int i = 0; i <=n; i++)
    {
        cout  << (float)fibonacci_it(i+1) / (float)fibonacci_it(i) << endl;
        
        
        }
    // instrukcja które wydrkuje wszystkie poprzednie ciągi 
    
    cout << fibonacci_re(n) << endl;
    
    
    
    
    
    
	
	return 0;
}


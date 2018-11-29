/*
 * Horner.cxx
 * 
 * Copyright 2018  <>


* W(x) = 2x^3 + 3x^2+5x+4 =>6
* w(x) x(2x^2 + 3x + 5) +4 
* W(x)= x(x(2x + 3) +5) + 4 => 3

 */


#include <iostream>

using namespace std;

void drukujw(int stopien, float tbwsp[])

{
    int x;
    for(int i = stopien; i <= 0; i--)
        cout << x << "^" << stopien;
   
    
    
    }

int main(int argc, char **argv)
{  
    float x = 0;
    float *tbwsp; // wskaźnik 
    int stopien = 0;
    cout << "Podaj stopień wielomianu";
    cin >> stopien;
    tbwsp = new float[stopien + 1];
    cout << tbwsp;
    for(int i=0; i <=stopien;){
        
        cout << "Podaj współczynniki przy potędze " << stopien-i << ": ";
        cin >> tbwsp[i];
        }
	
    cout << "Podaj argument:";
    cin >> x;
    
    cout << "Wartośc wielomianu o postaci:";
    void drukujw(stopien ,tbwsp);

    
    
    
	return 0;
}


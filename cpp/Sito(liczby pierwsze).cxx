/*
 * Sito(liczby pierwsze).cxx
 * 
 * Copyright 2018  <>
 */


#include <iostream>
#include <cmath>
using namespace std;


int main(int argc, char **argv)
{
   bool tablica[101];
   int i = 0;
   int j = 0;
   int zakres = 0;
   
   for (i=2; i < 101; i++)
   {
       
       tablica[i]= true;
       
       }
    cout <<"Podaj górny zareks,max.100:";
    cin >> zakres;
    float b = sqrt((float)zakres);
    for(i=2; i<= b; i++){
        
        if(tablica[i] != false)
            for(j = i + i; j < zakres + 1; j = j + i ){
                tablica[j] = false;
            
                }
        
        
        }
        
        if(tablica[i] = true){
    cout << i;
   }
	
    return 0;
}


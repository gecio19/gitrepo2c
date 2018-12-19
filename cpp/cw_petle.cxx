/*
 * cw_petle.cxx
 * 
 * Copyright 2018  <>

 */


#include <iostream>
using namespace std;



void voidcw01(){
 
 int n = 0;
 int suma = 0;
 while(suma < 75)
        {
            
           cout << "Podaj cyfre";
           cin >> n;
           suma = suma + n; 
            
            
            }
    cout << suma << endl;
    
    }
    
    
    
void voidcw02()
{
    int n = 0;
    int m = 0;
    cout << "Podaj Początek przedziału :";
    cin >> n;
    
    cout << "Podaj koniec przedziału :";
    cin >> m;
    
    
    for(int i = n; i <= m; i++)
    {
        cout << i << endl;
        
        }
    
    
    
    
    
    }    

void voidcw03()


{
    int n = 0;
    
    cout << "Podaj koniec przedzału :";
    cin >> n;
    n = n;
    int suma = 0;
    for(int i =0; i <= n; i++)
    
    {
        suma = i*i;
        cout << "Cos:" << suma << endl;
        
        }
    
    }


void voidcw04()

{
   
   
   for(int i=10; i <100; i++)
   
   {
       if((i%3 == 0) && (i%2 == 0))
       
           cout << "Liczby to:" << i;
       
   
    
    }
        
        
        
    
    
    
    
    


int main(int argc, char **argv)
{
	
    voidcw01();
    voidcw02();
    voidcw03();
    voidcw04();
	return 0;
}


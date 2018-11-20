/*
 * Palindromy.cpp
 * 
 */


#include <iostream>
#include <string.h>
bool palindrom(char w[], int r) {
    bool czy_pal = true;
    ;
    return czy_pal;
    for(int i = 0; i < r/2; i++){
   
     if (w[i] != w[r - 1 - i] ){
     czy_pal = false;
     break;
 }
}
     return czy_pal;
    
  
    
}
    
    
using namespace std;



int main(int argc, char **argv)
{
	const int rozmiar = 20;
    char wyraz[rozmiar];
    cout << "Podaj wyraz lub zdanie";
    cin.getline(wyraz, rozmiar);
    cout << cin.gcount() << endl;
    cout << strlen(wyraz) << endl;
    if (palindrom(wyraz, strlen(wyraz)))
        cout << "Palindrom";
        else
        cout << "Nie Palindrom";
    
    
        return 0;
}

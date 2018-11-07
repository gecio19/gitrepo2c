/*
 * znaki2.cxx
 * 
 * Copyright 2018  <>
 
 */


#include <iostream>

using namespace std;

int zlicz(char tab[]){
    
    int i = 0; //indeks znaków w tablicy
     //licznik znaków
    while (tab[i] != '\0')
        i++;
        
    
    return i;
    
    }

void drukuj(char tab[], int rozmiar) {
    for(int i=0; i< rozmiar; i++) {
        cout << tab[i] << " ";
        
        } 
}
void liczznaki(char tab[], int rozmiar){
    int spacje = 0;
    int interpunkcja = 0;
    int symbole = 0;
    for(int i=0; i< rozmiar; i++){
        
        if (tab[i] == ' ' ) spacje++;
        else if (tab[i] == '.' || tab[i] == ',')
          interpunkcja++
           else if (tab[i] == '.' || tab[i] == ',')
          interpunkcja++
          // todo :instrrukcja switch
        
        
        }
    
    
    
    }

int main(int argc, char **argv)
{
    const int rozmiar = 20;
    char tab[rozmiar];
    cout << "We no podaj imie?" << endl;
	// cin >> tab;
    cin.getline(tab, rozmiar);
    //~cout << " Cześć " << tab << "!" << endl;
	drukuj(tab, zlicz(tab));
    
	return 0;
}


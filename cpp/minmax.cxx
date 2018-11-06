/*
 * minmax.cxx

 */


#include <iostream>

using namespace std;

void wypelnij(int tab[], int roz) {
    cout << "Wprowadź rozmiar" << roz << "liczb: " << endl;
    for(int i=0; i<roz; i++) {
        cin >> tab[i];
        
        } 
    
}

void drukuj(int tab[], int roz) {
    for(int i=0; i<roz; i++) {
        cout << tab[i] << " " << endl;
        
        } 
    
}

void minmax(int tab[], int roz) {
    int minimum = tab[0];
    int maximum = tab[0];
    for(int i=1; i<roz; i++) {
        if (minimum > tab[i])
            minimum = tab[i];
        if (maximum < tab[i])
            maximum = tab[i]; 
            

        }
        
    cout << "liczba min =" << minimum << endl;
    cout << "liczba max =" << maximum << endl; 
    
}



int main(int argc, char **argv)
{
    const int rozmiar = 5;
    
    int tab[rozmiar];
    wypelnij (tab, rozmiar);
	drukuj (tab, rozmiar);
    cout << endl;
    minmax (tab, rozmiar);
	return 0;
}


/*
 * liczby23.cpp

 */



#include <iostream>

using namespace std;


int liczby2(){
    int ile = 0;
    for(int i = 1; i < 10;i++) {
        for(int j = 1; j <10; j++) {
            
            if (j != i) {
                    cout << i << j << " ";
                    ile++;
                }
            }
        }  
        return ile;
}
    


int liczby3(){
    int ile = 0;
    for(int i = 1; i < 10;i++) {
        for(int j = 1; j < 10; j++) {
			for(int k = 1; k < 10; k++){
            
            if (j != i != k != i) {
                    cout << i << j << k << " ";
                    ile++;
                }
            }
        }  
        
    }

        return ile;
	}

    













int main(int argc, char **argv)
{

	cout << "liczby 2 cyfrowe" << liczby2();
    cout << "\n\ " ;
    cout << "liczby 2 cyfrowe" << liczby3();

    
	return 0;
}


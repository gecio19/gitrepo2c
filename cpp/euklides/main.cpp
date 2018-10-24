#include <iostream>

using namespace std;

int nwd1(int a, int b) {

  while (a != b) {
    if (a > b)
        a = a - b;
    else
        b = b - a;
    }
          return a;
}



int main()
{

   int a, b;
   a = b = 0;
   cout << "Podaj 1.liczbę:";
   cin >> a >> b;
   cout << "NWD (" << a << ", " << b << ") = "
        << nwd1(a, b) << endl;





    return 0;
}

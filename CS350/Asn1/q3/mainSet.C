#include "Set.H"
using namespace std;

int main()
{
  Set a(64), b(64), c(64);
  Set d(65);
  
  a = b = c;

  a.add(1); a.add(5);
  b.add(3); b.remove(3);
  c.add(4); c.add(a);

  a.print(cout); cout << endl;
  b.print(cout); cout << endl;
  c.print(cout); cout << endl;

  //a.remove(d);
  a.complement();
  a.print(cout); cout << endl;
}

/* output:

[ 1 5 ]
[ ]
[ 1 4 5 ]
[ 0 2 3 4 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 ]

*/

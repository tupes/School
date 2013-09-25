#include <iostream>
#include "Rational.H"

using namespace std;

int main()
{
  typedef long long Int;
  typedef Rational<Int> Rat;

  // implicit type conversion int -> Int
  Rat r(-33,39), s(19,17);
  
  cout << r.value() << endl;
  cout << s.value() << endl;

  cout << (r+s) << endl;
  cout << (r-s) << endl;
  cout << (r*s) << endl;
  cout << (r/s) << endl;

  r += Rat(3,2); cout << r << endl;
  r -= Rat(2,3); cout << r << endl;
  r *= Rat(3,4); cout << r << endl;
  r /= Rat(4,3); cout << r << endl;
  cout << r++ << " " << r << endl;
  cout << --r << " " << r << endl;
  cout << ++r << " " << r << endl;
  cout << r-- << " " << r << endl;
  cout << r.get_num() << " " << r.get_den() << endl;
}

/* output
[60/221]
[-434/221]
[-209/221]
[-187/247]
[17/26]
[-1/78]
[-1/104]
[-3/416]
[-3/416] [413/416]
[-3/416] [-3/416]
[413/416] [413/416]
[413/416] [-3/416]
-3 416
*/

#include "Opt.H"
#include <iostream>
using namespace std;

// uncomment one for testing error conditions
//#define TEST_ERROR1
//#define TEST_ERROR2
//#define TEST_ERROR3

int main(int argc, char * argv[])
{
  Opt o;

  // add options
  o.add_switch("-a", "'switch on' option");
  o.add_bool  ("-b", "bool option",         false);
  o.add_int   ("-i", "int option",          800);
  o.add_int   ("-j", "another int option",  400);
  o.add_double("-d", "double option",       0.5);
  o.add_string("-s", "string option",       "default");

#ifdef TEST_ERROR1
  o.add_int   ("-i", "already defined", 1);
  // output:
  // opt: duplicate option -i
#endif
  
  // process command-line options
  o.process(argc, argv);

  // retrieve option values
  cout << "The following values will be used in the program:" << endl;

  bool   a = o.get_switch("-a");  cout << "a=" << a << endl;
  bool   b = o.get_bool  ("-b");  cout << "b=" << b << endl;
  int    i = o.get_int   ("-i");  cout << "i=" << i << endl;
  int    j = o.get_int   ("-j");  cout << "j=" << j << endl;
  double d = o.get_double("-d");  cout << "d=" << d << endl;
  string s = o.get_string("-s");  cout << "s=" << s << endl;

#ifdef TEST_ERROR2
  double x = o.get_double("-x");  cout << "x=" << x << endl;
  // output:
  // opt: tried to retrieve unknown option -x
#endif
  
#ifdef TEST_ERROR3
  double y = o.get_double("-a");  cout << "y=" << y << endl;
  // output:
  // opt: in get_double -a is not a double option
#endif
  
  return 0;
}

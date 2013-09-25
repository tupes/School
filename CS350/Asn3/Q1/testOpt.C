
#include "Opt.H"
using namespace std;

int main(int argc, char **argv)
{
  Opt o;

  // add options
  o.add("-i", 800,               "int option");
  o.add("-b", false,             "bool option");  
  //~ //o.add("-w", "'switch on' option (no third parameter)");
  o.add("-s", string("default"), "string option");  // note the type cast
  o.add("-d", 0.5,               "double option");

  // process command-line options
  o.process(argc, argv);

  // retrieve option values
  int    i = o.get<int>("-i");    cout << "i=" << i << endl;
  bool   b = o.get<bool>("-b");   cout << "b=" << b << endl;
  //~ //bool   w = o.get<bool>("-w");   cout << "w=" << w << endl;
  string s = o.get<string>("-s"); cout << "s=" << s << endl;
  double d = o.get<double>("-d"); cout << "d=" << d << endl;

#if 0
  float err = o.get<float>("-d", err); cout << "err=" << err << endl;
#endif
}
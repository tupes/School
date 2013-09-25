
#ifndef OPT_H
#define OPT_H

#include <cassert>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

/////////////////////////////////////////////////////////////
// Class which manages command line options for a program. //
/////////////////////////////////////////////////////////////

class Opt
{
public:

  Opt();
  ~Opt();

  // add_x functions
  template <typename T, typename V> void add_x(const std::string &n, const std::string &descr, V defaultValue);
  void add_switch(const std::string &name, const std::string &description);
  void add_bool(const std::string &name, const std::string &description, bool defaultValue);
  void add_int(const std::string &name, const std::string &description, int defaultValue);
  void add_double(const std::string &name, const std::string &description, double defaultValue);
  void add_string(const std::string &name, const std::string &description, const std::string &defaultValue);
  // get_x functions
  template <typename T, typename V> V get_value(const std::string &name, const std::string &type);
  bool get_switch(const std::string &name);
  bool get_bool(const std::string &name);
  int get_int(const std::string &name);
  double get_double(const std::string &name);
  std::string get_string(const std::string &name);
  // process
  void process(int argc, char * argv[]);

private:

  Opt(const Opt&) {}
  void operator=(const Opt&) {}
  
  // forward declaration of Option classes
  // define those classes in Opt.C
  class OptionBase;
  class SwitchOption;
  class BoolOption;
  class IntOption;
  class DoubleOption;
  class StringOption;
  
  // collection of added options
  // use option.push_back(p) to add new pointer
  // and options[i] to retrieve the i-th option
  // option.size() returns the current number of options
  std::vector<OptionBase*> options;

  // find option in vector by name
  OptionBase* find_option(const std::string &name);
  // print all options to cerr if name isn't found
  void unknown_option(const std::string &name);
};

#endif
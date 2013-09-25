
#ifndef OPT_H
#define OPT_H

#include <cassert>
#include <cstdlib>
#include <iostream>
#include <string>
#include <map>

/////////////////////////////////////////////////////////////
// Class which manages command line options for a program. //
/////////////////////////////////////////////////////////////

class Opt
{
public:

	Opt();
	~Opt();

	template <typename T> 
	void add(const std::string &n, const T &defaultValue, const std::string &descr) {
		// raise error if it's a duplicate
		//~ if (find_option(n)) {
			//~ std::cerr << "opt: duplicate option " << n << std::endl;
			//~ exit(20);
		//~ }
		// create a new Option and put it into the vector
		OptT<T>* o = new OptT<T>(n, defaultValue, descr);
		omap[n] = o;
	}

	template <typename T> 
	T get(const std::string &name) {
		OptionBase* o = omap[name];
		// make sure it was found
		//~ if (!o) {
			//~ std::cerr << "opt: tried to retrieve unknown option " << name << std::endl;
			//~ exit(20);
		//~ }
		// if this down-cast fails (i.e., returns 0) we know it's not the right type of option
		//OptT<T> *so = dynamic_cast<OptT<T>*>(o);
		//~ if (!so) {
			//~ cerr << "opt: in get " << name << " is not a option" << endl;
			//~ exit(20);
		//~ }
		//~ // otherwise, it's the right type of option
		return o.get_value();
	}
	// process
	void process(int argc, char * argv[]);

private:
	
	Opt(const Opt&) {}
	void operator=(const Opt&) {}

	// forward declaration of Option classes
	// define those classes in Opt.C
	class OptionBase {
	public:
		virtual ~OptionBase();
		//virtual get_value();
	};
	
	template <typename T>
	class OptT : public OptionBase {
	public:

		std::string name;   // name of option
		std::string descr;  // its description
		std::string type;   // the type of the subclass
		T value;

		OptT(const std::string &n, const T &defaultValue, const std::string &description) {
			name = n;
			value = defaultValue;
			descr = description;
			//type = t;
		}
		
		virtual ~OptT() {}
		
		T get_value() {
			return value;
		}
		
		//~ void update(std::string new_value, T value) {
			//~ std::istringstream in(new_value);
			//~ in >> *value;
			//~ // if the value is the wrong type or there's more after, raise error
			//~ if (in.fail() || !in.eof()) {
				//~ std::cerr << "opt: value syntax error for option " << name << " (" << new_value << ")" << std::endl;
				//~ exit(20);
			//~ }
		//~ }	
		
		void show() {
			std::cerr << name << " : " << descr << " [" << type << "] " << value << std::endl;
		}
	};
	class SwitchOption;
	class BoolOption;
	class IntOption;
	class DoubleOption;
	class StringOption;

	// collection of added options
	// use option.push_back(p) to add new pointer
	// and options[i] to retrieve the i-th option
	// option.size() returns the current number of options
	std::map<std::string, OptionBase*> omap;

	// find option in vector by name
	//OptionBase* find_option(const std::string &name);
	// print all options to cerr if name isn't found
	void unknown_option(const std::string &name);
};

#endif
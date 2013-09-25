#ifndef Opt_H
#define Opt_H

// Convenient command line option handling class,
// implemented with templates and inheritance

#include <cstdlib>
#include <iostream>
#include <sstream>
#include <string>
#include <map>


class Opt
{
public:

	// generic add
	template <typename T>
	void add(const std::string &n, const T &defaultValue, const std::string &descr){
		if (omap.find(n) != omap.end()) {
			std::cerr << "opt: duplicate option " << n << std::endl;
			exit(20);
		}
		OptT<T>* o = new OptT<T>(n, defaultValue, descr, 1);
		omap[n] = o;
	}

	// add switch option
	void add(const std::string &n, const std::string &descr) {
		if (omap.find(n) != omap.end()) {
			std::cerr << "opt: duplicate option " << n << std::endl;
			exit(20);
		}
		OptT<bool>* o = new OptT<bool>(n, 0, descr, 0);
		omap[n] = o;
	}

	// generic get
	template <typename T>
	T get(const std::string &name) {
		if (omap.find(name) == omap.end()) {
			std::cerr << "opt: tried to retrieve unknown option " << name << std::endl;
			exit(20);
		}
		OptT<T>* o = dynamic_cast<OptT<T>*>(omap[name]);
		if (!o) {
			// not quite right
			std::cerr << "opt: in get " << name << " is not a valid option" << std::endl;
			exit(20);
		}
		return o->value;
	}

	// parse command line arguments
	void process(int argc, char **argv);
	// if an unknown option is passed in through argv
	void unknown_option(const std::string &name);

	Opt() { }
	~Opt();

private:
	Opt(const Opt&) {}
	void operator=(const Opt&) {}
	// base class OptionBase
	class OptionBase {
	public:
		std::string name;
		std::string descr;
		bool needs_param;
		virtual ~OptionBase() {}
		virtual void update(const std::string &value) {}
		virtual void update() {}
		virtual void show() {}
	};

	// generic option class OptT
	template <class T> class OptT : public OptionBase {
	public:

		T value;
	
		OptT(const std::string &n, const T &defaultValue, const std::string &d, const bool &np) {
			name = n;
			descr = d;
			value = defaultValue;
			needs_param = np;
		}
		
		~OptT() {}

		void update(const std::string &new_value) {
			std::istringstream in(new_value);
			in >> value;
			// if the value is the wrong type or there's more after, raise error
			if (in.fail() || !in.eof()) {
				std::cerr << "opt: value syntax error for option " << name << " (" << new_value << ")" << std::endl;
				exit(20);
			}
		}
		
		// for updating the switch option
		void update() {
			value = 1;
		}
		
		// this is incomplete (missing type in brackets)
		void show() {
			std::cerr << name << " : " << descr << " [] " << value << std::endl;
		}
	};
	
	// associates option strings with option objects
	// Options must be stored in this container!
	// To print options in lexicographical order
	// just iterate through omap - it's a sorted
	// associative container.
	std::map<std::string, OptionBase*> omap;
};

#endif

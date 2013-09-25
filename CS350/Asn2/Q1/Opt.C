
#include "Opt.H"
#include <cstdlib>
#include <sstream>

using namespace std;

// option base-class
class Opt::OptionBase
{
public:

	string name;   // name of option
	string descr;  // its description
	string type;   // the type of the subclass

	OptionBase(const string &n, const string &description, const string &t) {
		name = n;
		descr = description;
		type = t;
	}
	
	virtual ~OptionBase() {}
	
	template <typename T> void update_x(string new_value, T value) {
		istringstream in(new_value);
		in >> *value;
		// if the value is the wrong type or there's more after, raise error
		if (in.fail() || !in.eof()) {
			cerr << "opt: value syntax error for option " << name << " (" << new_value << ")" << endl;
			exit(20);
		}
	}	
	
	template <typename T> void show_x(T value) {
		cerr << name << " : " << descr << " [" << type << "] " << value << endl;
	}
	
	// only functions which are type specific should be implemented in the subclass,
	// otherwise, we get unnecessary code duplication
	virtual void update(string) {}
	virtual void show() {}
};

struct Opt::SwitchOption : public Opt::OptionBase
{
	bool value;
	
	SwitchOption(const string &n, const string &description, bool)
	: OptionBase(n, description, "switch") {
		value = 0;
	}
	
	void update(string) {
		value = 1;
	}
	
	void show() {
		show_x("");
	}
};

struct Opt::BoolOption : public Opt::OptionBase
{
	bool value;
	
	BoolOption(const string &n, const string &description, bool defaultValue)
	: OptionBase(n, description, "bool") {
		value = defaultValue;
	}
	
	void update(string new_value) {
		update_x(new_value, &value);
	}
	
	void show() {
		show_x(value);
	}
};

struct Opt::IntOption : public Opt::OptionBase
{
	int value;
	
	IntOption(const string &n, const string &description, int defaultValue)
	: OptionBase(n, description, "int") {
		value = defaultValue;
	}
	
	void update(string new_value) {
		update_x(new_value, &value);
	}
	
	void show() {
		show_x(value);
	}
};

struct Opt::DoubleOption : public Opt::OptionBase
{
	double value;
	
	DoubleOption(const string &n, const string &description, double defaultValue)
	: OptionBase(n, description, "double") {
		value = defaultValue;
	}
	
	void update(string new_value) {
		update_x(new_value, &value);
	}

	void show() {
		show_x(value);
	}
};

struct Opt::StringOption : public Opt::OptionBase
{
	string value;
	
	StringOption(const string &n, const string &description, const string &defaultValue)
	: OptionBase(n, description, "string") {
		value = defaultValue;
	}
	
	// needed to delete value member
	~StringOption() {};
	
	void update(string new_value) {
		value = new_value;
	}
	
	void show() {
		show_x(value);
	}
};

// Opt member functions
Opt::Opt() {}

Opt::~Opt() {
	vector<OptionBase*>::iterator iter = options.begin(), end = options.end();
	for (; iter != end; ++iter)
		delete *iter;
}

void Opt::process(int argc, char * argv[]) {
	string value, name;
	int i = 1;
	while (i < argc) {
		name.assign(argv[i]);
		OptionBase* o = find_option(name);
		// raise error if name not found
		if (!o) 
			unknown_option(name);
		if (o->type != "switch") {
			// if it's not a switch option, the next token should be the value
			// first check to make sure there's another token
			if (i == argc - 1) {
				cerr << "opt: missing value" << endl << endl;
				exit(20);
			}
			++i;
			value.assign(argv[i]);
		}
		o->update(value);
		++i;
	}
}

Opt::OptionBase* Opt::find_option(const string &name) {
	// iterate through options, and if the name matches, return it
	vector<OptionBase*>::iterator iter = options.begin(), end = options.end();
	for (; iter != end; ++iter) {
		OptionBase* o = *iter;
		if (o->name == name)
			return o;
	}
	// unknown option, let caller deal with it since this function 
	// is used by three different functions
	return 0;
}

void Opt::unknown_option(const string &name) {
	// print out all of the options and their description to cerr
	cerr << "opt: unknown option " << name << endl << "choices are:" << endl;
	vector<OptionBase*>::iterator iter = options.begin(), end = options.end();
	for (; iter != end; ++iter) {
		OptionBase* o = *iter;
		o->show();
	}
	cerr << endl;
	exit(20);
}

// add_x functions
template <typename T, typename V> 
void Opt::add_x(const string &n, const string &descr, V defaultValue) {
	// raise error if it's a duplicate
	if (find_option(n)) {
		cerr << "opt: duplicate option " << n << endl;
		exit(20);
	}
	// create a new Option and put it into the vector
	T* o = new T(n, descr, defaultValue);
	options.push_back(o);
}

void Opt::add_switch(const string &n, const string &descr) {
	add_x<SwitchOption>(n, descr, 0);
}

void Opt::add_bool(const string &n, const string &descr, bool defaultValue) {
	add_x<BoolOption>(n, descr, defaultValue);
}

void Opt::add_int(const string &n, const string &descr, int defaultValue) {
	add_x<IntOption>(n, descr, defaultValue);
}

void Opt::add_double(const string &n, const string &descr, double defaultValue) {
	add_x<DoubleOption>(n, descr, defaultValue);
}

void Opt::add_string(const string &n, const string &descr, const string &defaultValue) {
	add_x<StringOption>(n, descr, defaultValue);
}

// get_x functions
template <typename T, typename V> 
V Opt::get_value(const string &name, const string &type) {
	OptionBase* o = find_option(name);
	// make sure it was found
	if (!o) {
		cerr << "opt: tried to retrieve unknown option " << name << endl;
		exit(20);
	}
	// if this down-cast fails (i.e., returns 0) we know it's not the right type of option
	T *so = dynamic_cast<T*>(o);
	if (!so) {
		cerr << "opt: in get_" << type << " " << name << " is not a " << type << " option" << endl;
		exit(20);
	}
	// otherwise, it's the right type of option
	return so->value;
}

bool Opt::get_switch(const string &name) {
	return get_value<SwitchOption, bool>(name, "switch");
}

bool Opt::get_bool(const string &name) {
	return get_value<BoolOption, bool>(name, "bool");
}

int Opt::get_int(const string &name) {
	return get_value<IntOption, int>(name, "int");
}

double Opt::get_double(const string &name) {
	return get_value<DoubleOption, double>(name, "double");
}

string Opt::get_string(const string &name) {
	return get_value<StringOption, string>(name, "string");
}


#include "Opt.H"
#include <cstdlib>
#include <sstream>

using namespace std;




//~ struct Opt::SwitchOption : public Opt::OptionBase
//~ {
	//~ SwitchOption(const string &n, const string &description, bool)
	//~ : OptionBase(n, description, "switch") {
		//~ value = 0;
	//~ }
	
	//~ void update(string) {
		//~ value = 1;
	//~ }
	
	//~ void show() {
		//~ show_x("");
	//~ }
//~ };

struct Opt::BoolOption : public Opt::OptT<bool>
{
	//~ BoolOption(const string &n, const string &description, bool defaultValue)
	//~ : OptionBase(n, description, "bool") {
		//~ value = defaultValue;
	//~ }
};

struct Opt::IntOption : public Opt::OptT<int>
{
	//~ IntOption(const string &n, const string &description, int defaultValue)
	//~ : OptionBase(n, description, "int") {
		//~ value = defaultValue;
	//~ }
};

struct Opt::DoubleOption : public Opt::OptT<double>
{
	//~ DoubleOption(const string &n, const string &description, double defaultValue)
	//~ : OptionBase(n, description, "double") {
		//~ value = defaultValue;
	//~ }
};

struct Opt::StringOption : public Opt::OptT<string>
{
	//~ StringOption(const string &n, const string &description, const string &defaultValue)
	//~ : OptionBase(n, description, "string") {
		//~ value = defaultValue;
	//~ }
	
	//~ void update(string new_value) {
		//~ value = new_value;
	//~ }
};

//~ // Opt member functions
Opt::Opt() {}

Opt::~Opt() {
	//~ vector<OptionBase*>::iterator iter = options.begin(), end = options.end();
	//~ for (; iter != end; ++iter)
		//~ delete *iter;
}

void Opt::process(int argc, char * argv[]) {
	string value, name;
	int i = 1;
	while (i < argc) {
		//~ name.assign(argv[i]);
		//~ OptionBase* o = find_option(name);
		//~ // raise error if name not found
		//~ if (!o) 
			//~ unknown_option(name);
		//~ if (o->type != "switch") {
			//~ // if it's not a switch option, the next token should be the value
			//~ // first check to make sure there's another token
			//~ if (i == argc - 1) {
				//~ cerr << "opt: missing value" << endl << endl;
				//~ exit(20);
			//~ }
			//~ ++i;
			//~ value.assign(argv[i]);
		//~ }
		//~ o->update(value);
		++i;
	}
}

//~ Opt::OptionBase* Opt::find_option(const string &name) {
	//~ // iterate through options, and if the name matches, return it
	//~ vector<OptionBase*>::iterator iter = options.begin(), end = options.end();
	//~ for (; iter != end; ++iter) {
		//~ OptionBase* o = *iter;
		//~ if (o->name == name)
			//~ return o;
	//~ }
	//~ // unknown option, let caller deal with it since this function 
	//~ // is used by three different functions
	//~ return 0;
//~ }

//~ void Opt::unknown_option(const string &name) {
	//~ // print out all of the options and their description to cerr
	//~ cerr << "opt: unknown option " << name << endl << "choices are:" << endl;
	//~ vector<OptionBase*>::iterator iter = options.begin(), end = options.end();
	//~ for (; iter != end; ++iter) {
		//~ OptionBase* o = *iter;
		//~ o->show();
	//~ }
	//~ cerr << endl;
	//~ exit(20);
//~ }



// Opt implementation

#include "Opt.H"

using namespace std;

Opt::~Opt()
{
	map<string, OptionBase*>::iterator iter = omap.begin(), end = omap.end();
	for (; iter != end; ++iter) {
		delete iter->second;
	}
}


// read options from command line
void Opt::process(int argc, char **argv) {
	string value, name;
	int i = 1;
	while (i < argc) {
		name.assign(argv[i]);
		if (omap.find(name) == omap.end())
			unknown_option(name);
		OptionBase* o = omap[name];
		if (o->needs_param) {
			// if it's not a switch option, the next token should be the value
			// first check to make sure there's another token
			if (i == argc - 1) {
				cerr << "opt: missing value" << endl << endl;
				exit(20);
			}
			++i;
			value.assign(argv[i]);
			o->update(value);
		}
		else
			o->update();
		++i;
	}
}

void Opt::unknown_option(const string &name) {
	// print out all of the options and their description to cerr
	cerr << "opt: unknown option " << name << endl << "choices are:" << endl;
	map<string, OptionBase*>::iterator iter = omap.begin(), end = omap.end();
	for (; iter != end; ++iter) {
		OptionBase* o = iter->second;
		o->show();
	}
	cerr << endl;
	exit(20);
}

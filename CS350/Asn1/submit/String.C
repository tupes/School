
#include "String.H"
using namespace std;

// constructor
String::String(const char *p) {
	shared = new SharedCString;
	shared->n = strlen(p);
	shared->count = 1;
	shared->data = new char[shared->n + 1];
	strncpy(shared->data, p, shared->n); 
}

// destructor
String::~String() {
	shared->count -= 1;
	if (shared->count < 1) {
		delete[] shared->data;
		delete shared;
	}
}

// copy constructor
String::String(const String &x) {
	shared = x.shared;
	shared->count += 1;
}

// assignment operator
String& String::operator=(const String &x) {
	delete[] shared->data;
	delete shared;
	shared = x.shared;
	shared->count += 1;
	return *this;
}

int String::size() const {
	return shared->n;
}

int String::ref_count() const {
	return shared->count;
}

const char* String::cstr() const {
	return shared->data;
}



#include <stdlib.h>
#include <stdio.h>
#include "Set.H"


Set::Set(int max_num) {
	bits = new int[max_num];
	n = max_num;
	a = 0;
	clear();
}

Set::~Set() {
	delete bits;
}

Set::Set(const Set &s) {
	bits = new int[s.n];
	n = s.n;
	a = 0;
	clear();
	add(s);
}

// STILL TO DO
Set& Set::operator=(const Set &s) {
	
	return *this;
}
/////////////////////////////

void Set::clear() {
	for (int i = 0; i < n; i++) {
		bits[i] = 0;
	}
}

void Set::complement() {
	for (int i=0; i < n; i++) {
		bits[i] = (bits[i] - 1) * -1;
	}
	a = n - a;
}

bool Set::has(int x) const {
	check_arg(x);
	return bits[x];
}

void Set::add(int x) {
	check_arg(x);
	bits[x] = 1;
	a += 1;
}

void Set::remove(int x) {
	check_arg(x);
	bits[x] = 0;
	a -= 1;
}

void Set::add(const Set &s) {
	//check_arg(s);
	assert(n == s.n);
	for (int i=0; i < n; i++) {
		if (s.bits[i] && !bits[i]) {
			bits[i] = 1;
			a += 1;
		}
	}
}

void Set::remove(const Set &s) {
	assert(n == s.n);
	for (int i=0; i < n; i++) {
		if (s.bits[i] && bits[i]) {
			bits[i] = 0;
			a -= 1;
		}
	}
}

void Set::print(std::ostream &os) const {
	os << "[";
	for (int i=0; i < n; i++) {
		if (bits[i])
			os << " " << i;
	}
	os << " ]";
}
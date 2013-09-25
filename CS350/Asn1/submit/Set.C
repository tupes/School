
#include "Set.H"

Set::Set(int max_num) {
	a = get_num_ints(max_num) + 1;
	bits = new int[a]();
	n = max_num;
}

Set::~Set() {
	delete[] bits;
}

Set::Set(const Set &s) {
	a = s.a;
	bits = new int[a]();
	n = s.n;
	add(s);
}

Set& Set::operator=(const Set &s) {
	delete[] bits;
	a = s.a;
	bits = new int[a]();
	n = s.n;
	add(s);
	return *this;
}

void Set::clear() {
	for (int i = 0; i < a; i++)
		bits[i] = 0;
}

void Set::complement() {
	for (int i = 0; i < a; i++)
		bits[i] = ~bits[i];
}

bool Set::has(int x) const {
	check_arg(x);
	return (1 << x) & bits[get_num_ints(x)];
}

void Set::add(int x) {
	check_arg(x);
	bits[get_num_ints(x)] |= (1 << x);
}

void Set::remove(int x) {
	check_arg(x);
	bits[get_num_ints(x)] &= ~(1 << x);
}

void Set::add(const Set &s) {
	assert(n == s.n);
	for (int i = 0; i < a; i++)
		bits[i] |= s.bits[i];
}

void Set::remove(const Set &s) {
	assert(n == s.n);
	for (int i = 0; i < a; i++)
		bits[i] &= ~(s.bits[i]);
}

void Set::print(std::ostream &os) const {
	os << "[";
	for (int i=0; i < n; i++) {
		if (has(i))
			os << " " << i;
	}
	os << " ]";
}

int get_num_ints(int max_num) {
  return (max_num / INT_BITS);
}

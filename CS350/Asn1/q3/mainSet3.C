
#include "Set.H"
using namespace std;

int main() {
	// create empty set
	Set a(200);
	a.print(cout); cout << endl;
	// add a bunch of legal elements
	a.add(5); a.add(29); a.add(102); a.add(199);
	a.print(cout); cout << endl;
	// remove some that are in the set, and others that aren't
	a.remove(102); a.remove(50);
	a.print(cout); cout << endl;
	// clear it
	a.clear();
	a.print(cout); cout << endl;
	// add more stuff for copying testing
	a.add(10); a.add(75); a.add(139); a.add(199);
	a.print(cout); cout << endl;
	
	// copy construct a new set
	Set b = a;
	b.print(cout); cout << endl;
	// add some new stuff
	b.add(55); b.add(180);
	b.print(cout); cout << endl;
	// remove a from b
	b.remove(a);
	b.print(cout); cout << endl;
	
	// create new set for testing assignment
	Set c(50);
	c.print(cout); cout << endl;
	c = a;
	c.print(cout); cout << endl;
	c.add(b);
	c.print(cout); cout << endl;
	// complement
	c.complement();
	c.print(cout); cout << endl;
	
	// fail cases
	Set d(50);
	//d.add(a);
	//d.add(c);
	//d.add(70);
	
	return 0;
}

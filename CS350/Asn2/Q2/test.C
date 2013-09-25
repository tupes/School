
#include <iostream>
#include "ListStack.H"
using namespace std;

int main() {
	ListStack<int> stack;
	cout << "empty: " << stack.empty() << endl;
	stack.push(5);
	stack.push(6);
	stack.push(7);
	cout << "size: " << stack.size() << endl;
	cout << "empty: " << stack.empty() << endl;
	cout << "top: " << stack.top() << endl;
	
	// test copy constructor
	cout << "testing CC" << endl;
	ListStack<int> s2 = stack;
	cout << "size: " << s2.size() << endl;
	cout << "empty: " << s2.empty() << endl;
	cout << "top: " << s2.top() << endl;
	
	// make sure independent
	stack.pop();
	cout << "top: " << stack.top() << endl;
	stack.pop();
	
	cout << "size: " << stack.size() << endl;
	cout << "empty: " << stack.empty() << endl;
	cout << "top: " << stack.top() << endl;
	
	cout << "size: " << s2.size() << endl;
	cout << "empty: " << s2.empty() << endl;
	cout << "top: " << s2.top() << endl;
	
	// test assignment
	cout << "testing =" << endl;
	stack = s2;
	cout << "size: " << stack.size() << endl;
	cout << "empty: " << stack.empty() << endl;
	cout << "top: " << stack.top() << endl;
	
	
	cout << "Finished" << endl;
	return 0;
}
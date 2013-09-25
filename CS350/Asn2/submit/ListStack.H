
#ifndef ListStack_H
#define ListStack_H

#include <cassert>

template <typename T> 
class ListStack 
{
public:
	// constructor
	ListStack() {
		head = 0; // the bottom of the stack doesn't point to anything
		n = 0;
	}

	// destructor: calls the Node destructor which is recursive
	~ListStack() {
		delete head;
	}

	// copy constructor: calls the Node CC which is recursive
	ListStack(const ListStack& other) {
		n = other.n;
		if (other.empty())
			head = 0;
		else 
			head = new Node(*(other.head));
	}

	// assignment operator: calls the Node CC which is recursive
	ListStack& operator= (const ListStack &other) {
		if (this == &other) return *this;
		// clean up memory
		delete head;
		n = other.n;
		if (other.empty())
			head = 0;
		else
			head = new Node(*(other.head));
		return *this;
	}

	// add an element at the top of the stack
	void push(const T& value) {
		head = new Node(value, head);
		++n;
	}
	
	// remove top element (pre-cond: !empty)
	void pop() {
		assert(n);
		// create a reference to the current head to delete
		Node* popped = head;
		// set the head to the next node
		head = head->next;
		// unlink the popped node to avoid chain deleting
		popped->next = 0;
		delete popped;
		--n;
	}
	
	// true iff no element present
	bool empty() const {
		return n == 0;
	}
	
	// return current number of elements
	int size() const {
		return n;
	}
	
	// return reference to top element (pre-cond: !empty)
	T& top() {
		assert(n);
		return head->data;
	}
	// return reference to top element in const context (pre-cond: !empty)
	const T& top() const {
		assert(n);
		return head->data;
	}

private:

	// each node stores a generic piece of data and a pointer to the next
	// node down the ListStack	
	class Node {
	public:
		T data;
		Node* next;

		// constructor: creates link to previous head
		Node(T value, Node* node) {
			data = value;
			next = node;
		}
		
		// copy constructor: recursively copy constructs nodes until it
		// reaches the bottom of the other ListStack
		Node(const Node &node) {
			data = node.data;
			if (node.next) 
				next = new Node(*(node.next));
			else
				next = 0;
		}
		
		// doesn't need AO because Node is private and I'm not using AO
		
		// recursively deletes all linked nodes
		~Node() {
			delete next;
		}
	};

	Node *head;            // pointer to head node of linked list
	int n;                 // number of elements
};

#endif


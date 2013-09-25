#ifndef Set_H
#define Set_H

#include <cassert>
#include <iostream>
#include <stdlib.h>
#include <stdio.h>

// represents a set of integers 0..n-1

static const int INT_BITS = sizeof(int) * 8;

class Set
{
public:

  Set(int n);                   // create empty subset of {0..n-1}
  ~Set();                       // destructor
  Set(const Set &s);            // copy constructor
  Set& operator=(const Set &s); // assignment operator

  void clear();              // empty set
  void complement();         // negate set (x was in set before <=> x is not in set after)
  bool has(int x) const;     // return true iff x is element of set (0 <= x < n)
  void add(int x);           // add element x to set (0 <= x < n)
  void remove(int x);        // remove element x from set (0 <= x < n)

  // add all elements of s to set; pre-cond: s.n == n
  void add(const Set &s);

  // remove all elements of s from set; pre-cond: s.n == n
  void remove(const Set &s);
  
  // return maximum number of elements
  int get_n() const { return n; }
  
  // print elements to output stream os like so: 
  // [ 1 2 4 5 ]
  // for set {1,2,4,5} (no extra spaces, no newline characters)
  void print(std::ostream &os = std::cout) const;
  
private:

  int *bits; // array of integers storing bits (x in set <=> bit x = 1)
  int n;     // max. number of elements (elements are 0,1,...n-1)
  int a;     // number of allocated ints
  
  // raise an assertion error if not 0 <= x < n
  void check_arg(int x) const {
    assert(x >= 0); assert(x < n);
  }
};

// find out how many ints are required to store the max_num number of bits
int get_num_ints(int max_num);

#endif
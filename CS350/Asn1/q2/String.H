#ifndef String_H
#define String_H

#include <iostream>
#include <string.h>

class String
{
public:

  // constructor: initializes String with copy of 0-terminated C-string  
  String(const char *p);
  
  // destructor: frees shared resources if possible  
  ~String();

  // copy constructor  
  String(const String &x);

  // assignment operator  
  String &operator=(const String &x); 
  
  // return number of non-0 characters in string
  int size() const;

  // return reference count
  int ref_count() const;
  
  // returns pointer to character array
  const char *cstr() const;
  
private:

  struct SharedCString
  {
    char *data; // 0-terminated char array
    int n;      // number of non-0 characters in string
    int count;  // reference count, how many Strings share this object?
  };
  
  SharedCString *shared;
};

#endif

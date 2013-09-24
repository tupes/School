/* name:               		Mark Tupala
ONE Card number:    	1188594
Unix id:            		tupala
lecture section:    		B1
instructor's name:  		Dr. Martin Muller
lab section:        		H02
TA's name:          		Aditya Bhargava
*/

// Miscellaneous functions and vars that could be used in many programs

#ifndef UTILS_H
#define UTILS_H

#include <stdio.h>
#include <math.h>
#include <string.h>
#include <time.h>

// Macros:
#define MAX_FILENAME_LEN 128
#define PCLOSE_ERROR -1


// Global variables:
// name of the program being run, from argv[0]
extern char progName[];
// name of input file being given as argument, from argv[1]
extern char inputName[];
// name of the program to which information is sent.
extern const char execName[];
// for keeping track of the current line in the input file
extern long long lineNumber;

// Non-C99 compliant function prototypes:
long int lround(double x);
size_t strnlen(const char *s, size_t maxlen);
FILE *popen(const char *name, const char *mode);
int pclose(FILE *stream);

// Function prototypes:

void getSeed();
int randInt(int max);
// print startup message: time started and name of input file
void printIntro(void);
int areEqualFloats(double x, double y);

// simply prints error message with name of program and line number
void reportError(void);

// print msg and culprit (if not NULL), and call exit(EXIT_FAILURE)
void funcError(const char *msg, const char *culprit);

// closes inputfile and pipe
void closeFiles(FILE *in, FILE *executable);

#endif
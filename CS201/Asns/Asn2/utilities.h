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

#include "matrix.h"

// Macros:
#define MAX_FILENAME_LEN 128
#define PI acos(-1.0)

// Global variables:
// name of the program being run, from argv[0]
extern char progName[];
// name of input file being given as argument, from argv[1]
extern char inputName[];
// for keeping track of the current line in the input file
extern long long lineNumber;

// Non-C99 compliant function prototypes:
long int lround(double x);
size_t strnlen(const char *s, size_t maxlen);

// Function prototypes:

// print startup message: time started and name of input file
void printIntro(void);

// rotate coordinates by the appropriate amount
void rotateCoords(double *coords, double angle);

// simply prints error message with name of program and line number
void reportError(void);

// print msg and culprit (if not NULL), and call exit(EXIT_FAILURE)
void funcError(const char *msg, const char *culprit);

// closes inputfile and pipe
void closeFiles(FILE *inputfile, FILE *executable);

#endif
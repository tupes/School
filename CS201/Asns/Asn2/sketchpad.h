/* name:               		Mark Tupala
ONE Card number:    	1188594
Unix id:            		tupala
lecture section:    		B1
instructor's name:  		Dr. Martin Muller
lab section:        		H02
TA's name:          		Aditya Bhargava
*/

// Functions and vars for interacting with Sketchpad.jar executable
// through a passed pipe

#ifndef SKETCH_H
#define SKETCH_H

#include "matrix.h"

// Macros:
#define PCLOSE_ERROR -1

// Global variables:
// name of the program to which information is sent.
extern const char execName[];

// Non-C99 compliant function prototypes:
FILE *popen(const char *name, const char *mode);
int pclose(FILE *stream);

// Function prototypes:

// send the coords of the struct matrix through the appropriate
// commands to the executable
void drawMatrix(struct matrix *matptrs, FILE *executable);

// send everything on line after 'send' to executable
void send(char *line, FILE *executable);

#endif
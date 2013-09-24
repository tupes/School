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

#include <stdio.h>

#include "coordGeometry.h"

// Macros:
#define MAX_LINE_LEN 256

FILE *exec;
FILE *inputfile;

// Function prototypes:

// send the coords of the struct matrix through the appropriate
// commands to the executable
void changeImage(struct Location *loc, char command);
void changeFlame(struct Location *loc, struct Point *flame, char command);
void createFuel(int fuel);
void eraseFuel(int fuel);
void sendEnd();
#endif
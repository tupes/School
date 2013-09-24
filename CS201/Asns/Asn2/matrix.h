/* name:               		Mark Tupala
ONE Card number:    	1188594
Unix id:            		tupala
lecture section:    		B1
instructor's name:  		Dr. Martin Muller
lab section:        		H02
TA's name:          		Aditya Bhargava
*/

// Functions and vars for creating, accessing, and manipulating 
// struct matrix variables

#ifndef MATRIX_H
#define MATRIX_H

#include "utilities.h"

// Macros:
#define MAX_MATNAME_LEN 128
#define MAX_MATS 5
#define MAX_POINTS 5

// Global variables:

// a struct for holding all of the information pertaining to one matrix
struct matrix
{
	char name[MAX_MATNAME_LEN + 1];
	double *coords;
	long long coordCount;
	long long maxPoints;
};

// Function prototypes:

// create and initialize a struct matrix var, dynamically allocate
// memory for its coords, and put it in the matptr array
void initMatrix(struct matrix *matptr);

// store the name, coords, and coord count in the struct matrix var
int storeMatrix(struct matrix *matptr, char *name, FILE *inputfile);

// attempt to match name of matrix with matrices
// stored in matptr. return index if found, else -1
int findMatrix(struct matrix *matptr, char *matName, long long matCount);

// identify the xshift and yshift and add them to the
// coords stored in the struct
int shiftMatrix(struct matrix *matptr, char *line);

// identify the angle in degrees, convert it to radians, and change
// the coords stored in the struct accordingly
int rotateMatrix(struct matrix *matptr, char *line);

// print the matrix's coords to stdout
void printMatrix(struct matrix *matptrs);

// free all memory being used for struct matrix vars
void freeMats(struct matrix *matptr, long long matCount);

// always called after reportError(), sends 'end' to sketchpad,
// frees all memory, closes files, and calls exit(EXIT_FAILURE)
void cleanup(struct matrix *matptr, long long matCount, FILE *inputfile, 
	FILE *executable);

#endif
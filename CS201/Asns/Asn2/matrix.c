/* name:               		Mark Tupala
ONE Card number:    	1188594
Unix id:            		tupala
lecture section:    		B1
instructor's name:  		Dr. Martin Muller
lab section:        		H02
TA's name:          		Aditya Bhargava
*/

// Functions for creating, accessing, and manipulating 
// struct matrix variables

#include <stdio.h>
#include <string.h>
#include <math.h>
#include "memwatch.h"
#include "utilities.h"
#include "sketchpad.h"
#include "parse.h"
#include "matrix.h"

// create and initialize a struct matrix var, dynamically allocate
// memory for its coords, and put it in the matptr array
void initMatrix(struct matrix *matptr)
{	
	struct matrix mat;
	mat.maxPoints = MAX_POINTS;
	mat.coords = malloc(mat.maxPoints * 2 * sizeof(double));
	if (mat.coords == NULL)
		funcError("Unable to allocate memory", NULL);
 
	*matptr = mat;
}


// store the name, coords, and coord count in the struct matrix var
int storeMatrix(struct matrix *mat, char *name, FILE *inputfile)
{
	// store name
	if (sscanf(name, "%s", mat->name) == EOF)
		funcError("Could not read from string", NULL);
	// strings for storing line and token info
	char line[MAX_LINE_LEN + 1];
	char first[MAX_LINE_LEN + 1];
	char endName[MAX_LINE_LEN + 1];
	// initialize strings and index to 0's 
	clear(line); clear(first); clear(endName);
	long long ii = 0;
	
	// read lines from inputfile until "End Matrix" line
	while (fgets(line, MAX_LINE_LEN + 1, inputfile) != NULL)
	{
		// try to grab the first three tokens
		if (sscanf(line, "%s%*s%s", first, endName) == EOF)
			; // if none grabbed, skip blank line
		
		// if it's a comment, print it
		else if (strncmp(first, "#", 1) == 0)
			printf("%s", line);
		
		// if it starts with 'End', break out to return to parse()
		else if (strncmp(first, "End\0", 4) == 0)
			break;
		
		// otherwise, store the coords
		else
		{
			// check to see if you have enough memory
			if (ii >= (mat->maxPoints * 2))
			{
				mat->maxPoints *= 2;
				mat->coords = realloc(mat->coords, 
					mat->maxPoints * 2 * sizeof(double));
				if (mat->coords == NULL)
					funcError("Unable to allocate enough "
						"memory", NULL);
			}
			if (sscanf(line, "%lf%lf", &(mat->coords[ii]), 
				&(mat->coords[ii + 1])) == 2)
			
				ii += 2;
			else
				// there must be a command or unknown token
				return 1;
		}
		lineNumber++;
		// reset memory for while loop
		clear(line); clear(first); clear(endName);
	}
	if (ferror(inputfile) != 0)
		funcError("Error reading from file", inputName);
	
	// return error if names don't match
	if (strcmp(mat->name, endName) != 0)
		return 1;
	
	// store the number of coordinates for the matrix
	mat->coordCount = ii;
	return 0;
}

// attempt to match name of matrix with matrices
// stored in matptr. return index if found, else -1
int findMatrix(struct matrix *matptrs, char *matName, long long matCount)
{
	int nameLen = 0, thisLen = 0;
	nameLen = strnlen(matName, MAX_MATNAME_LEN);
	
	for (long long ii = 0; ii < matCount; ii++)
	{
		thisLen = strnlen(matptrs[ii].name, MAX_MATNAME_LEN);
		if (thisLen == nameLen &&
			strncmp(matptrs[ii].name, matName, nameLen) == 0)
			
			return ii;
	}
	return -1;
}

// identify the xshift and yshift and add them to the
// coords stored in the struct
int shiftMatrix(struct matrix *mat, char *line)
{
	double xshift = 0, yshift = 0;
	
	if (sscanf(line, "%*s%*s%lf%lf", &xshift, &yshift) == 2)
	{
		for (long long ii = 0; ii < mat->coordCount; ii += 2)
		{
			mat->coords[ii] += xshift;
			mat->coords[ii + 1] += yshift;
		}
	}
	else
		// there must be an unknown token
		return 1;
	
	return 0;
}

// identify the angle in degrees, convert it to radians, and change
// the coords stored in the struct accordingly
int rotateMatrix(struct matrix *mat, char *line)
{
	double angleDegrees = 0, angleRadians = 0;
	
	if (sscanf(line, "%*s%*s%lf", &angleDegrees) == 1)
	{
		angleRadians = angleDegrees * PI / 180.0;
		
		for (long long ii = 0; ii < mat->coordCount; ii += 2)
		{
			rotateCoords(&mat->coords[ii], angleRadians);
		}
	}
	else
		// there must be an unknown token
		return 1;
	
	return 0;
}

// print the matrix's coords to stdout
void printMatrix(struct matrix *mat)
{
	printf("Print Matrix %s =\n", mat->name);
	
	for (long long ii = 0; ii < mat->coordCount; ii += 2)
	{
		printf("%g %g\n", 
			mat->coords[ii], mat->coords[ii + 1]);
	}
	
	printf("End Matrix %s\n", mat->name);
}

// free all memory being used for struct matrix vars
void freeMats(struct matrix *matptr, long long matCount)
{
	for (long long ii = 0; ii < matCount; ii++)
		free(matptr[ii].coords);
	free(matptr);
}

// always called after reportError(), sends 'end' to sketchpad,
// frees all memory, closes files, and calls exit(EXIT_FAILURE)
void cleanup(struct matrix *matptr, long long matCount, \
	FILE *inputfile, FILE *executable)
{
	char command[] = "send end\n";
	send(command, executable);
	freeMats(matptr, matCount);
	closeFiles(inputfile, executable);
	exit(EXIT_FAILURE);
}
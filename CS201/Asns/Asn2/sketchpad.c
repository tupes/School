/* name:               		Mark Tupala
ONE Card number:    	1188594
Unix id:            		tupala
lecture section:    		B1
instructor's name:  		Dr. Martin Muller
lab section:        		H02
TA's name:          		Aditya Bhargava
*/

// Functions for interacting with Sketchpad.jar executable
// through a passed pipe

#include <stdio.h>
#include <string.h>
#include "memwatch.h"
#include "utilities.h"
#include "matrix.h"
#include "parse.h"
#include "sketchpad.h"

// send the coords of the struct matrix through the appropriate
// commands to the executable
void drawMatrix(struct matrix *mat, FILE *executable)
{
	long x1 = 0, y1 = 0, x2 = 0, y2 = 0;
	
	for (int ii = 0; ii < (mat->coordCount - 2); ii += 2)
	{
		x1 = lround(mat->coords[ii]);
		y1 = lround(mat->coords[ii + 1]);
		x2 = lround(mat->coords[ii + 2]);
		y2 = lround(mat->coords[ii + 3]);
		fprintf(executable, "drawSegment %ld %ld %ld %ld\n", 
			x1, y1, x2, y2); 
	}
}

// send every char after 'send' on the line to the executable
void send(char *line, FILE *executable)
{
	char command[MAX_LINE_LEN];
	int length = strnlen(line, MAX_LINE_LEN);
	
	for (int ii = 4; ii <= length; ii++)
		command[ii - 4] = line[ii];
	
	fprintf(executable, "%s", command);
}
/* name:               		Mark Tupala
ONE Card number:    	1188594
Unix id:            		tupala
lecture section:    		B1
instructor's name:  		Dr. Martin Muller
lab section:        		H02
TA's name:          		Aditya Bhargava
*/

// for parsing the input file and carrying out the appropriate actions

#include <stdio.h>
#include <string.h>
#include "memwatch.h"
#include "matrix.h"
#include "sketchpad.h"
#include "utilities.h"
#include "parse.h"

// reads each line in the inputfile, identifies at least the
// first token, and calls the appropriate function
void parse(FILE* inputfile, FILE* executable)
{	
	// some counter vars need to be as large as possible
	long long maxMats = MAX_MATS, matCount = 0, index = 0;
	// flag for calling reportError and cleanup
	int isError;
	// dynamically allocated struct matrix array
	struct matrix *matptr = malloc(maxMats * sizeof(struct matrix));
	if (matptr == NULL)
		funcError("Unable to allocate memory", NULL);
	// strings for storing line and token info
	char line[MAX_LINE_LEN + 1];
	char first[MAX_LINE_LEN + 1];
	char name[MAX_LINE_LEN + 1];
	// initialize strings to 0's, and lineNumber to 1
	clear(line); clear(first); clear(name);
	lineNumber = 1;
	
	// get line from file until EOF is reached
	while (fgets(line, MAX_LINE_LEN + 1, inputfile) != NULL)
	{
		if (filter(line, first, name, executable))
		{
			// grab the matrix's index in matptr, if it's there
			index = findMatrix(matptr, name, matCount);
			// if line is declaring a matrix, store its info
			if (strncmp(first, "Matrix\0", 7) == 0)
			{
				// if index is <0, it hasn't been defined
				if (index < 0)
				{
					index = matCount;
					// if index is at maxMats, realloc mem
					if (index >= maxMats)
					{
						maxMats *= 2;
						matptr = realloc(matptr, 
							maxMats * 
							sizeof(struct matrix));
						if (matptr == NULL)
							funcError("Unable to "
								"allocate "
								"enough "
								"memory", 
								NULL);
					}
					matCount++;
					initMatrix(&matptr[index]);
				}
				isError = storeMatrix(&matptr[index], name, 
					inputfile);
			}
			else
			{
				// check to see if the matrix has been defined
				if (index < 0)
					isError = 1;
				else
					// call the appropriate function
					isError = callMatFunc(&matptr[index], 
						first, line, executable);
			}
			if (isError)
			{
				reportError();
				cleanup(matptr, matCount, inputfile, 
					executable);
			}
		}
		lineNumber++;
		// reset memory for while loop
		clear(line); clear(first); clear(name);
	}
	if (ferror(inputfile) != 0)
		funcError("Error reading from file", inputName);
	
	// free all memory
	freeMats(matptr, matCount);
}

// determines whether the line needs further parsing by filtering
// out blank lines, comments, and send commands
int filter(char line[], char first[], char name[], FILE *executable)
{
	// try to grab the first two tokens
	if (sscanf(line, "%s%s", first, name) == EOF)
		; // blank line
		
	// if its a comment, print it
	else if (strncmp(first, "#", 1) == 0)
		printf("%s", line);
		
	// if it's a send command, send it
	else if (strncmp(first, "send\0", 5) == 0)
		send(line, executable);
	
	else
		// if none of the above, we need to further parse the line
		return 1;
	
	return 0;
}

// call appropriate matrix function based on command
int callMatFunc(struct matrix *matptr, char command[], char line[], 
	FILE *executable)
{
	int isError = 0;
	
	if (strncmp(command, "drawMatrix\0", 11) == 0)
		drawMatrix(matptr, executable);
	
	else if (strncmp(command, "printMatrix\0", 12) == 0)
		printMatrix(matptr);

	else if (strncmp(command, "shift\0", 6) == 0)
		isError = shiftMatrix(matptr, line);
	else if (strncmp(command, "rotate\0", 7) == 0)
		isError = rotateMatrix(matptr, line);
	else
		// unknown first token
		return 1;
	
	return isError;
}

// convenience function for setting strings to all 0's
void clear(char *line)
{
	memset(line, 0, MAX_LINE_LEN + 1);
}
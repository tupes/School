/* name:               		Mark Tupala
ONE Card number:    	1188594
Unix id:            			tupala
lecture section:    		B1
instructor's name:  		Dr. Martin Muller
lab section:        			H02
TA's name:          			Aditya Bhargava
*/

/* 
Reads each line of an input file given as an argument,
and takes the appropriate action based on the type of line,
including sending commands to Sketchpad.jar, storing data
in memory, and printing to stdout.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "draw1b.h"

// global variables:
// name of the program being run, from argv[0]
char progName[MAX_NAME_LEN + 1];
// name of input file being given as argument, from argv[1]
char inputName[MAX_NAME_LEN + 1];
// name of the program to which information is sent.
const char execName[] = "java -jar Sketchpad.jar";

// responsible for opening input file and pipe, calling
// parse() with those arguments, and closing file and pipe
int main(int argc, char *argv[])
{
	// store names of the program and input file in globals
	memset(progName, 0, MAX_NAME_LEN + 1);
	strncpy(progName, argv[0], MAX_NAME_LEN);
	memset(inputName, 0, MAX_NAME_LEN + 1);
	strncpy(inputName, argv[1], MAX_NAME_LEN);
	
	// check for correct number of arguments
	if (argc != MAX_NUM_ARGS + 1)
		printError("Incorrect number of arguments", NULL);
	
	// open file
	FILE * inputfile = fopen(inputName, "r");
	if (inputfile == NULL)
		printError("Could not open file", inputName);
	
	// open pipe
	FILE * executable = popen(execName, "w");
	if (executable == NULL)
		printError("Could not open pipe", execName);
	
	// print startup message
	printIntro();
	
	// read, identify, and execute each line in the input file
	parse(inputfile, executable);
	
	// close file and pipe and call exit
	if (fclose(inputfile) == EOF)
		printError("Could not close file", inputName);
	if (pclose(executable) == PCLOSE_ERROR)
		printError("Could not close pipe", execName);
	
	exit(EXIT_SUCCESS);
}

// reads each line in the inputfile, identifies at least the
// first token, and calls the appropriate function
void parse(FILE* inputfile, FILE* executable)
{	
	// strings for storing line and token info
	char line[MAX_LINE_LEN + 1];
	char first[MAX_LINE_LEN + 1];
	char name[MAX_LINE_LEN + 1];
	// initialize strings and ints to 0's
	clear(line); clear(first); clear(name);
	int matCount = 0, index = 0;
	
	// get line from file until EOF is reached
	while (fgets(line, MAX_LINE_LEN + 1, inputfile) != NULL)
	{
		// grab the first two tokens
		if (sscanf(line, "%s%s", first, name) == EOF)
			printError("Unable to read from string", line);
		
		// if its a comment, print it
		if (strncmp(first, "#", 1) == 0)
			printf("%s", line);
		
		// if it's a send command, send it
		else if (strncmp(first, "send", 4) == 0)
			send(line, executable);
		
		else
		{
			// grab the matrix's index in matList, if it's there
			index = findMatrix(name, matCount);
			
			// if line is declaring a matrix, store its info
			if (strncmp(first, "Matrix", 6) == 0)
			{
				// if index is <0, it hasn't been defined
				if (index < 0)
					index = matCount;
				storeMatrix(name, index, inputfile);
				matCount++;
			}
			else
			{
				// call the appropriate function
				if (strncmp(first, "shift", 5) == 0)
					shiftMatrix(index, line);
				else if (strncmp(first, "draw", 4) == 0)
					drawMatrix(index, executable);
				else if (strncmp(first, "print", 5) == 0)
					printMatrix(index);
				else
					printError("Unknown line in file", 
							inputName);
			}
		}
		// reset memory for while loop
		clear(line); clear(first); clear(name);
	}
	if (ferror(inputfile) != 0)
		printError("Error reading from file", inputName);
}

// use the index 'm' to store the name, coords, and coord count
// in the appropriate struct in the matList
void storeMatrix(char *name, int m, FILE *inputfile)
{
	if (sscanf(name, "%s", matList[m].name) == EOF)
		printError("Unable to read from string", name);
	memset(matList[m].coords, 0, MAX_NUM_POINTS * 2);
	int ii = 0;
	// strings for storing line and token info
	char line[MAX_LINE_LEN + 1];
	char first[MAX_LINE_LEN + 1];
	clear(line); clear(first);
	
	// read lines from inputfile until "End Matrix" line
	while (fgets(line, MAX_LINE_LEN + 1, inputfile) != NULL &&
				sscanf(line, "%s", first) == 1 &&
				strncmp(first, "End", 3) != 0)
	{
		// if it's a comment, print it
		if (strncmp(first, "#", 1) == 0)
			printf("%s", line);
		
		// otherwise, store the coords
		else
		{
			if (sscanf(line, "%lf%lf", &matList[m].coords[ii], 
				&matList[m].coords[ii + 1]) == 2)
			
				ii += 2;
			else
				printError("Unable to read from string", line);
		}
		// reset memory for while loop
		clear(line); clear(first);
	}
	if (ferror(inputfile) != 0)
		printError("Error reading from file", inputName);
	
	// store the number of coordinates for the matrix
	matList[m].coordCount = ii;
}

// attempt to match name of matrix with matrices
// stored in matList. return index if found, else -1
int findMatrix(char *matName, int matCount)
{
	int nameLen = 0, thisLen = 0;
	nameLen = strnlen(matName, MAX_MATRIX_LEN);
	
	for (int ii = 0; ii < matCount; ii++)
	{
		thisLen = strnlen(matList[ii].name, MAX_MATRIX_LEN);
		if (thisLen == nameLen &&
			strncmp(matList[ii].name, matName, nameLen) == 0)
			
			return ii;
	}
	return -1;
}

// identify the xshift and yshift and add them to the
// coords stored in the struct given by index 'm'
void shiftMatrix(int m, char *line)
{
	double xshift = 0, yshift = 0;
	
	if (sscanf(line, "%*s%*s%lf%lf", &xshift, &yshift) == 2)
	{
		for (int ii = 0; ii < matList[m].coordCount; ii += 2)
		{
			matList[m].coords[ii] += xshift;
			matList[m].coords[ii + 1] += yshift;
		}
	}
	else
		printError("Unable to read from string", line);
}

// use the index 'm' to print the appropriate info to stdout
void printMatrix(int m)
{
	printf("Print Matrix %s =\n", matList[m].name);
	
	for (int ii = 0; ii < matList[m].coordCount; ii += 2)
	{
		printf("%g %g\n", 
			matList[m].coords[ii], matList[m].coords[ii + 1]);
	}
	
	printf("End Matrix %s\n", matList[m].name);
}

// use the index 'm' to construct and send the appropriate
// commands to the executable
void drawMatrix(int m, FILE *executable)
{
	long x1 = 0, y1 = 0, x2 = 0, y2 = 0;
	
	for (int ii = 0; ii < (matList[m].coordCount - 2); ii += 2)
	{
		x1 = lround(matList[m].coords[ii]);
		y1 = lround(matList[m].coords[ii + 1]);
		x2 = lround(matList[m].coords[ii + 2]);
		y2 = lround(matList[m].coords[ii + 3]);
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

// print time and inputfile name on startup
void printIntro(void)
{
	printf("./draw1b started on ");
	fflush(NULL);
	system("date\n");
	printf("Input file: %s\n", inputName);
}

// convenience function for setting strings to all 0's
void clear(char *line)
{
	memset(line, 0, MAX_LINE_LEN + 1);
}

// print an error message given as argument and the name of the
// file (if not NULL), and then call exit
void printError(const char *msg, const char *culprit)
{
	fprintf(stderr, "%s:  %s", progName, msg);
	if (culprit != NULL)
		fprintf(stderr, " (%s)", culprit);
	fprintf(stderr, "\n");
	exit(EXIT_FAILURE);
}

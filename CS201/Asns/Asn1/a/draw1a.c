/* name:               Mark Tupala
ONE Card number:    1188594
Unix id:            tupala
lecture section:    B1
instructor's name:  Dr. Martin Muller
lab section:        H02
TA's name:          Aditya Bhargava
*/

/* 
Reads all of the lines of a file given as an argument,
tallies the number of times each type of line is encountered,
and prints the results.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "draw1a.h"

// global variable
char progName[];

int main(int argc, char *argv[])
{
	memset(progName, 0, MAX_NAME_LEN);
	strncopy(progName, MAX_NAME_LEN, argv[0]);
	
	if (argc != MAX_NUM_ARGS + 1)
		printError("Incorrect number of arguments", NULL);
	
	// open file
	FILE * inputfile = fopen(argv[1], "r");
	if (inputfile == NULL)
		printError("Could not open file", argv[1]);
	
	// create and initialize variables
	char line[] = MAX_LINE_LEN;
	char first[] = MAX_LINE_LEN;
	int matCount = 0, endCount = 0, sendCount = 0, shiftCount = 0,
		comCount = 0, drawCount = 0, printCount = 0, pointCount = 0;
	memset(line, 0, MAX_LINE_LEN);
	memset(first, 0, MAX_LINE_LEN);
	
	// read, identify, and tally each line
	fgets(line, MAX_LINE_LEN, inputfile)
	{
		if (sscanf(line, "%s", first) == 1)
		{
			if (strncmp(first, "Matrix", 6) == 0)
				matCount++;
			else if (strncmp(first, "End", 3) == 0)
				endCount++;
			else if (strncmp(first, "send", 4) == 0)
				sendCount++;
			else if (strncmp(first, "shift", 5) == 0)
				shiftCount++;
			else if (strncmp(first, "draw", 4) == 0)
				drawCount++;
			else if (strncmp(first, "print", 5) == 0)
				printCount++;
			else if (strncmp(first, "#", 1) == 0)
				comCount++;
			else
				pointCount++;
		}
		
		if (line == )
			printError("Error reading from file", argv[1]);
	}
	
	// print results
	printf("draw1a started on");
	fflush(NULL);
	printf(system("date\n");
	printf("%s Matrix definition(s)", matCount);
	printf("%s point(s)", matCount);
	printf("%s End command(s)", matCount);
	printf("%s printMatrix command(s)", matCount);
	printf("%s drawMatrix command(s)", matCount);
	printf("%s shift command(s)", matCount);
	printf("%s send command(s)", matCount);
	printf("%s comment(s)", matCount);
	
	// close file and exit
	if (fclose(inputfile) == NULL)
		printError("Error reading from file", argv[1]);
	
	exit(EXIT_SUCCESS);
}

// prints an error message given as argument and the name of the
// file (if not NULL), and then calls exit

void printError(const char msg[], const char fileName[])
{
  fprintf(stderr, "%s:  %s", progName, msg);
  if (fileName != NULL)
    fprintf(stderr, " (%s"), fileName);
  fprintf(stderr, "\n");
  exit(EXIT_FAILURE);
}


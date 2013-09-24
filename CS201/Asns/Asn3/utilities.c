/* name:               		Mark Tupala
ONE Card number:    	1188594
Unix id:            		tupala
lecture section:    		B1
instructor's name:  		Dr. Martin Muller
lab section:        		H02
TA's name:          		Aditya Bhargava
*/

// Miscellaneous functions and vars that could be used in many programs

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
//#include "sketchpad.h"
#include "utilities.h"

// Global variable:
// for keeping track of the current line in the input file
long long lineNumber = 0;

// Functions:
int areEqualFloats(double x, double y)
{
	if (fabs(x - y) < 0.0001)
		return 1;
	return 0;
}

// print time and inputfile name on startup
void printIntro(void)
{
	printf("%s started on ", progName);
	fflush(NULL);
	system("date\n");
	printf("Input file: %s\n", inputName);
}

	
// simply prints error message with name of program and line number
void reportError(void)
{
	fprintf(stderr, "%s: %lld, error.\n", progName, lineNumber);
}

// print an error message given as argument and the name of the
// file (if not NULL), and then call exit
void funcError(const char *msg, const char *culprit)
{
	fprintf(stderr, "%s:  %s", progName, msg);
	if (culprit != NULL)
		fprintf(stderr, " (%s)", culprit);
	fprintf(stderr, "\n");
	exit(EXIT_FAILURE);
}

// closes inputfile and pipe
void closeFiles(FILE *inputfile, FILE *executable)
{	
	if (fclose(inputfile) == EOF)
		funcError("Could not close file", inputName);
	
	if (pclose(executable) == PCLOSE_ERROR)
		funcError("Could not close pipe", execName);
}

void getSeed()
{
	time_t t;
	t = time(NULL);
	srand(t);
}

int randInt(int max)
{
	return rand() % max + 1;
}
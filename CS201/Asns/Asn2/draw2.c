/* name:               		Mark Tupala
ONE Card number:    	1188594
Unix id:            		tupala
lecture section:    		B1
instructor's name:  		Dr. Martin Muller
lab section:        		H02
TA's name:          		Aditya Bhargava
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
#include "memwatch.h"
#include "matrix.h"
#include "sketchpad.h"
#include "utilities.h"
#include "parse.h"

#define MAX_NUM_ARGS 1

// Global variables:
// name of the program being run, from argv[0]
char progName[MAX_FILENAME_LEN + 1];
// name of input file being given as argument, from argv[1]
char inputName[MAX_FILENAME_LEN + 1];
// name of the program to which information is sent.
const char execName[] = "java -jar Sketchpad.jar";

// responsible for opening input file and pipe, calling
// parse() with those arguments, and returning successfully
int main(int argc, char *argv[])
{
	// store names of program and input file in globals from utilities.h
	memset(progName, 0, MAX_FILENAME_LEN + 1);
	strncpy(progName, argv[0], MAX_FILENAME_LEN + 1);
	memset(inputName, 0, MAX_FILENAME_LEN + 1);
	strncpy(inputName, argv[1], MAX_FILENAME_LEN + 1);
	
	// check for correct number of arguments
	if (argc != MAX_NUM_ARGS + 1)
	{
		reportError();
		exit(EXIT_FAILURE);
	}
	
	// open file
	FILE * inputfile = fopen(inputName, "r");
	if (inputfile == NULL)
	{
		reportError();
		exit(EXIT_FAILURE);
	}
	
	// open pipe
	FILE * executable = popen(execName, "w");
	if (executable == NULL)
		funcError("Could not open pipe", execName);
	
	// print startup message
	printIntro();
	
	// read, identify, and execute each line in the input file
	parse(inputfile, executable);
	
	// clean up and call exit
	closeFiles(inputfile, executable);	
	exit(EXIT_SUCCESS);
}

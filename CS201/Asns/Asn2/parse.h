/* name:               		Mark Tupala
ONE Card number:    	1188594
Unix id:            		tupala
lecture section:    		B1
instructor's name:  		Dr. Martin Muller
lab section:        		H02
TA's name:          		Aditya Bhargava
*/

// for parsing the input file and carrying out the appropriate actions

#ifndef PARSE_H
#define PARSE_H

// Macros:
#define MAX_LINE_LEN 256

// Function protoypes:

// reads each line in the inputfile, identifies at least the
// first token, and calls the appropriate function
void parse(FILE* inputfile, FILE* executable);

// determines whether the line needs further parsing by filtering
// out blank lines, comments, and send commands
int filter(char line[], char first[], char name[], FILE *executable);

// call appropriate matrix function based on command
int callMatFunc(struct matrix *matptr, char command[], char line[], 
	FILE *executable);
	
// convenience function for setting strings to all 0's
void clear(char *line);

#endif
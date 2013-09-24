/* name:	 Mark Tupala	
// ONE card number: 1188594
// Unix id: tupala
// lecture session: B1
// instructor's name: Dr. Martin Muller
// lab section: H02
// TA's name: Aditya Bhargava
*/

#ifndef PARSE_H
#define PARSE_H

// Macros:
#define MAX_NAME_LEN 128
#define MAX_LINE_LEN 256
#define NUM_ARGS 1

// Global variables:
extern char progName[];
/* The name of the program to which information is sent. */
extern const char execName[];

// Global structs:
extern struct matrix
{
	char name[MAX_NAME_LEN];
	double coords[MAX_POINTS * 2];
	int count;
};

/* Non-C99 compliant function prototypes. */
FILE *popen(const char *command, const char *type);
int pclose(FILE *stream);
long int lround(double x);

// Function declarations:

// prints msg and fileName (if not NULL), and calls exit(EXIT_FAILURE)
void printError(const char msg[], const char fileName[]);

#endif
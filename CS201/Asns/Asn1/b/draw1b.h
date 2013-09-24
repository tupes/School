/* name:	 			Mark Tupala	
// ONE card number: 	1188594
// Unix id: 			tupala
// lecture session: 		B1
// instructor's name: 	Dr. Martin Muller
// lab section: 			H02
// TA's name: 			Aditya Bhargava
//
// header file for draw1b.c. Contains macros, global variables,
// non-c99 compliant function prototypes, and my function prototypes
*/

#ifndef DRAW1B_H
#define DRAW1B_H

// Macros:
#define MAX_NAME_LEN 128
#define MAX_MATRIX_LEN 128
#define MAX_LINE_LEN 256
#define MAX_NUM_MATRIX 16
#define MAX_NUM_POINTS 16
#define MAX_NUM_ARGS 1
#define PCLOSE_ERROR -1

// Global variables:
// name of the program being run, from argv[0]
extern char progName[];
// name of input file being given as argument, from argv[1]
extern char inputName[];
// name of the program to which information is sent.
extern const char execName[];

// Global struct:
// an array of structs, with each struct capable of storing the 
// data from one matrix
struct matrix
{
	char name[MAX_MATRIX_LEN + 1];
	double coords[MAX_NUM_POINTS * 2];
	int coordCount;
} matList[MAX_NUM_MATRIX];

// Non-C99 compliant function prototypes:
FILE *popen(const char *name, const char *mode);
int pclose(FILE *stream);
long int lround(double x);
size_t strnlen(const char *s, size_t maxlen);

// Function prototypes:
// parse inputfile and call the appropriate function
void parse(FILE* inputfile, FILE* executable);

// use index to store name, coords, number of coords in struct
void storeMatrix(char *name, int index, FILE *inputfile);

// look for matrix name in matList. return index if found, else -1
int findMatrix(char *matName, int matCount);

// parse line for shift amounts, use index to change coords in struct
void shiftMatrix(int index, char *line);

// use index to print the appropriate coords to stdout
void printMatrix(int index);

// use index to send the appropriate coords to executable
void drawMatrix(int index, FILE *executable);

// send everything on line after 'send' to executable
void send(char *line, FILE *executable);

// print startup message: time started and name of input file
void printIntro(void);

// set arg string to all 0's by calling memset. simply saves space
void clear(char *line);

// print msg and culprit (if not NULL), and call exit(EXIT_FAILURE)
void printError(const char *msg, const char *culprit);

#endif

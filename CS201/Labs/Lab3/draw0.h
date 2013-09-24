/*
 * Declarations and macros for draw0.c.
 *
 * See draw0.c for more information.
 */
#ifndef DRAW0_H // "include guard" prevents double inclusions
#define DRAW0_H

#define MAX_LINE_LEN 256

/* Declaration for string storing name of executable.  
   Also see definition in draw0.c for more info. 
*/
extern const char Exec_c[];

/* Represents a point */
struct point
{
  double x;
  double y;
};

/* Prototypes for non-standard-library functions */
FILE* popen(const char*, const char*);
int pclose(FILE*);

#endif // DRAW0_H

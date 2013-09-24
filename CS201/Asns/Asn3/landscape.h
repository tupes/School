/* name:               		Mark Tupala
ONE Card number:    	1188594
Unix id:            		tupala
lecture section:    		B1
instructor's name:  		Dr. Martin Muller
lab section:        		H02
TA's name:          		Aditya Bhargava
*/

#ifndef LANDSCAPE
#define LANDSCAPE

#include "coordGeometry.h"
#include "physics.h"


struct Asteroid
{
	struct Location loc;
	struct Kinetic kin;
	int exists;
};

struct Environment
{
	struct Location land;
	struct Asteroid asteroid;
};

struct Location land;

void genAsteroid();
void storeLand(struct Location *landptr, FILE *input);
int detectCollision(struct Location *ship, struct Location *land);
int isFlat(struct Location *land);
#endif
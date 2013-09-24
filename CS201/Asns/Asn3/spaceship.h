/* name:               		Mark Tupala
ONE Card number:    	1188594
Unix id:            		tupala
lecture section:    		B1
instructor's name:  		Dr. Martin Muller
lab section:        		H02
TA's name:          		Aditya Bhargava
*/

#ifndef SPACESHIP
#define SPACESHIP

#include "coordGeometry.h"
#include "physics.h"

#define EDGE_LEN 20
#define SPEED_THRESHOLD 8
#define FLAME_SIZE 5
#define FUEL_AMOUNT 300

struct spaceship
{
	struct Location loc;
	struct Kinetic kin;
	struct Point flame;
	float thrust;
	float gravity;
	int thrustOn;
	int fuel;
}ship;

void createShip(struct spaceship *ship, float thrust, float gravity);
void createFlame(struct spaceship *ship);
void accelShip(struct spaceship *ship);
// IMPROVEMENT
void accelShipWithFuel(struct spaceship *ship);
void translateShip(struct spaceship *ship, double displaceX, double displaceY);
void checkBoundaries(struct spaceship *ship);
void rotateShip(struct spaceship *ship, int angleChange);
//void shiftCoords(struct spaceship *shipptr, double hor, double vert);
int checkLanding(struct spaceship *ship, struct Location *land);
void execCritical();
void execCritical_2();
void execCriticalSecondary();
void gameOver();

void	translateAst(struct Location *loc, double displaceX, double displaceY);

#endif
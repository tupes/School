/* name:               		Mark Tupala
ONE Card number:    	1188594
Unix id:            		tupala
lecture section:    		B1
instructor's name:  		Dr. Martin Muller
lab section:        		H02
TA's name:          		Aditya Bhargava
*/

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#include "keyboard.h"
#include "physics.h"
#include "utilities.h"
#include "sketchpad.h"
#include "landscape.h"
#include "spaceship.h"

struct Environment enviro;

void createShip(struct spaceship *shipptr, float thrust, float gravity)
{
	struct spaceship ship;
	ship.thrust = thrust;
	ship.gravity = gravity;
	//ship.loc.centre.x = 635;
	ship.loc.centre.x = 315;
	ship.loc.centre.y = 35;
	double shift = EDGE_LEN / 2;
	double halfshift = shift / 2;
	//printf("shift %lf\n", shift);
	
	ship.loc.vertex[0].x = -shift;
	ship.loc.vertex[0].y = shift;
	
	ship.loc.vertex[1].x = shift;
	ship.loc.vertex[1].y = shift;
	
	ship.loc.vertex[2].x = halfshift;
	ship.loc.vertex[2].y = -shift;
	
	ship.loc.vertex[3].x = -halfshift;
	ship.loc.vertex[3].y = -shift;
	
	ship.loc.vertexCount = 4;
	
	createEdges(&(ship.loc));
	connectEnds(&(ship.loc));
	
	ship.flame.x = 0;
	ship.flame.y = ship.loc.vertex[0].y + FLAME_SIZE;
	createDetour(&ship.loc, &ship.flame);

	ship.loc.angle = 90;
	
	ship.kin.xVel = 0;
	ship.kin.yVel = 0;
	ship.kin.xAcc = 0;
	ship.kin.yAcc = 0;
	
	ship.thrustOn = 0;
	ship.fuel = FUEL_AMOUNT;
	
	*shipptr = ship;
}

void execCritical_2()
{
	double displaceY = applyForce(&ship.kin.yVel, ship.kin.yAcc + ship.gravity);
	double displaceX = applyForce(&ship.kin.xVel, ship.kin.xAcc);
	translateShip(&ship, displaceX, displaceY);
	if (detectCollision(&ship.loc, &land))
	{
		char msg;
		if (checkLanding(&ship, &land))
			msg = 'L';
		else
			msg = 'C';
		
		printOutcome(msg);
		gameOver();
	}
	ship.kin.yAcc = 0; ship.kin.xAcc = 0;
	// ASTEROID
	if (enviro.asteroid.exists)
	{
		displaceY = applyForce(&enviro.asteroid.kin.yVel, 0);
		displaceX = applyForce(&enviro.asteroid.kin.xVel, 0);
		translateAst(&enviro.asteroid.loc, displaceX, displaceY);
		if (detectCollision(&ship.loc, &enviro.asteroid.loc))
		{
			printOutcome('C');
			gameOver();
		}
		if (detectCollision(&enviro.land, &enviro.asteroid.loc))
			enviro.asteroid.exists = 0;
	}
}

void execCritical()
{
	double displaceY = applyForce(&ship.kin.yVel, ship.kin.yAcc + ship.gravity);
	double displaceX = applyForce(&ship.kin.xVel, ship.kin.xAcc);
	translateShip(&ship, displaceX, displaceY);
	if (detectCollision(&ship.loc, &land))
	{
		char msg;
		if (checkLanding(&ship, &land))
			msg = 'L';
		else
			msg = 'C';
		
		printOutcome(msg);
		gameOver();
	}
	ship.kin.yAcc = 0; ship.kin.xAcc = 0;
}

void execCriticalSecondary()
{
	genAsteroid(&enviro);
}

void accelShip(struct spaceship *ship)
{
	double radians = angleRadians(ship->loc.angle);
	ship->kin.xAcc = -ship->thrust * cos(radians);
	ship->kin.yAcc = ship->thrust * sin(radians);
	ship->thrustOn = 1;
}

void accelShipWithFuel(struct spaceship *ship)
{
	if (ship->fuel > 0)
	{
		accelShip(ship);
		eraseFuel(ship->fuel);
		ship->fuel -= 1;
	}
}

void translateShip(struct spaceship *ship, double displaceX, double displaceY)
{
	changeFlame(&ship->loc, &ship->flame, 'E');
	changeImage(&ship->loc, 'E');
	shiftPoint(&ship->loc.centre, displaceX, displaceY);
	// IMPROVEMENT
	checkBoundaries(ship);
	// *****************
	changeImage(&ship->loc, 'D');
	if (ship->thrustOn)
	{
		changeFlame(&ship->loc, &ship->flame, 'D');
		ship->thrustOn = 0;
	}
}

void	translateAst(struct Location *loc, double displaceX, double displaceY)
{
	changeImage(loc, 'E');
	shiftPoint(&loc->centre, displaceX, displaceY);
	// IMPROVEMENT
	//checkBoundaries(ship);
	// *****************
	changeImage(loc, 'D');

}

void checkBoundaries(struct spaceship *ship)
{
	if (ship->loc.centre.y < 0)
	{
		ship->loc.centre.y = 0;
		ship->kin.yVel = 0;
	}
	if (ship->loc.centre.x < 0)
	{
		ship->loc.centre.x = 635;
	}
	else if (ship->loc.centre.x > 635)
	{
		ship->loc.centre.x = 0;
	}
}

void rotateShip(struct spaceship *ship, int angleChange)
{
	changeFlame(&ship->loc, &ship->flame, 'E');
	changeImage(&ship->loc, 'E');
	double radChange = angleRadians(angleChange);
	
	if (ship->loc.angle == 0 && angleChange > 0)
		ship->loc.angle = 350;
	else if (ship->loc.angle == 360 && angleChange < 0)
		ship->loc.angle = 10;
	else
		ship->loc.angle -= angleChange;
	
	for (int ii = 0; ii < ship->loc.vertexCount; ii++)
		rotatePoint(&(ship->loc.vertex[ii]), radChange);
	
	rotatePoint(&ship->flame, radChange);
	
	createEdges(&ship->loc);
	connectEnds(&ship->loc);
	createDetour(&ship->loc, &ship->flame);
	changeImage(&ship->loc, 'D');
	if (ship->thrustOn)
	{
		changeFlame(&ship->loc, &ship->flame, 'D');
		ship->thrustOn = 0;
	}

}

int checkLanding(struct spaceship *ship, struct Location *land)
{
	if (ship->kin.yVel > SPEED_THRESHOLD)
		return 0;
	
	else if (ship->loc.angle != 90)
		return 0;
	
	else if (!isFlat(land))
		return 0;
	
	return 1;
}

void gameOver()
{	
	// clean up and call exit
	unset_curses();
	printf("hit at %d degrees going %lf on a %d surface\n", ship.loc.angle, ship.kin.yVel, isFlat(&land));
	sendEnd();
	closeFiles(exec, inputfile);
	exit(EXIT_SUCCESS);
}
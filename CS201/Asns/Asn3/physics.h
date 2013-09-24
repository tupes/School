/* name:               		Mark Tupala
ONE Card number:    	1188594
Unix id:            		tupala
lecture section:    		B1
instructor's name:  		Dr. Martin Muller
lab section:        		H02
TA's name:          		Aditya Bhargava
*/

#ifndef PHYSICS_H
#define PHYSICS_H

#define INTERVAL 0.05

struct Kinetic
{
	double xVel;
	double yVel;
	double xAcc;
	double yAcc;
};

double applyForce(double *vel, float force);

#endif
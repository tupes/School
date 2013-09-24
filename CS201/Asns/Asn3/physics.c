/* name:               		Mark Tupala
ONE Card number:    	1188594
Unix id:            		tupala
lecture section:    		B1
instructor's name:  		Dr. Martin Muller
lab section:        		H02
TA's name:          		Aditya Bhargava
*/

#include "physics.h"

double applyForce(double *vel, float force)
{
	double accel = force * INTERVAL;
	double displace = (*vel * INTERVAL) + (0.5 * accel * INTERVAL);
	*vel += accel;
	return displace;
}


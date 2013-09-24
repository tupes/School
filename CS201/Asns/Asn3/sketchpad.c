/* name:               		Mark Tupala
ONE Card number:    	1188594
Unix id:            		tupala
lecture section:    		B1
instructor's name:  		Dr. Martin Muller
lab section:        		H02
TA's name:          		Aditya Bhargava
*/

// Functions for interacting with Sketchpad.jar executable
// through a passed pipe

#include <stdio.h>
#include <string.h>
#include <math.h>
//#include "spaceship.h"
//#include "landscape.h"
#include "sketchpad.h"


// send the coords of the struct matrix through the appropriate
// commands to the executable

void changeImage(struct Location *loc, char command)
{
	long x1 = 0, y1 = 0, x2 = 0, y2 = 0;
	int ii = 0;
	char sketchCommand[12];
	memset(sketchCommand, 0, 12);
	if (command == 'D')
		strncpy(sketchCommand, "drawSegment\0", 12);
	else if (command == 'E')
		strncpy(sketchCommand, "eraseSegment\0", 13);
	
	for (ii = 0; ii < loc->vertexCount; ii++)
	{
		x1 = lround(loc->edge[ii].pointA.x + loc->centre.x);
		y1 = lround(loc->edge[ii].pointA.y + loc->centre.y);
		x2 = lround(loc->edge[ii].pointB.x + loc->centre.x);
		y2 = lround(loc->edge[ii].pointB.y + loc->centre.y);
		fprintf(exec, "%s %ld %ld %ld %ld\n", 
			sketchCommand, x1, y1, x2, y2);
	}
	fflush(exec);
}

void changeFlame(struct Location *loc, struct Point *flame, char command)
{
	long x1 = 0, y1 = 0, x2 = 0, y2 = 0;
	char sketchCommand[12];
	memset(sketchCommand, 0, 12);
	if (command == 'D')
		strncpy(sketchCommand, "drawSegment\0", 12);
	else if (command == 'E')
		strncpy(sketchCommand, "eraseSegment\0", 13);
	
	x1 = lround(loc->edge[4].pointA.x + loc->centre.x);
	y1 = lround(loc->edge[4].pointA.y + loc->centre.y);
	x2 = lround(loc->edge[4].pointB.x + loc->centre.x);
	y2 = lround(loc->edge[4].pointB.y + loc->centre.y);
	fprintf(exec, "%s %ld %ld %ld %ld\n", 
		sketchCommand, x1, y1, x2, y2);

	x1 = lround(loc->edge[5].pointA.x + loc->centre.x);
	y1 = lround(loc->edge[5].pointA.y + loc->centre.y);
	x2 = lround(loc->edge[5].pointB.x + loc->centre.x);
	y2 = lround(loc->edge[5].pointB.y + loc->centre.y);
	fprintf(exec, "%s %ld %ld %ld %ld\n", 
		sketchCommand, x1, y1, x2, y2);
	
	fflush(exec);
}

void createFuel(int fuel)
{
	int y1 = 5, y2 = 10;
	for (int x = 1; x <= fuel; x++)
		fprintf(exec, "drawSegment %d %d %d %d\n", 
			x, y1, x, y2);
	fflush(exec);
}

void eraseFuel(int fuel)
{
	int y1 = 5, y2 = 10;
	fprintf(exec, "eraseSegment %d %d %d %d\n", 
		fuel, y1, fuel, y2);
	fflush(exec);
}

void sendEnd()
{
	char line[] = "end\n";
	fprintf(exec, "%s", line);
}





















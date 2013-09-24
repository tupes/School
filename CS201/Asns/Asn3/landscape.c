/* name:               		Mark Tupala
ONE Card number:    	1188594
Unix id:            		tupala
lecture section:    		B1
instructor's name:  		Dr. Martin Muller
lab section:        		H02
TA's name:          		Aditya Bhargava
*/

// for storing the landscape information in a struct matrix
// for use in drawing and detecting collision

#include <stdio.h>
#include "utilities.h"
#include "landscape.h"

// parse the input file for the landscape's coords and store
// them in a struct matrix

void storeLand(struct Location *land, FILE *input)
{
	land->vertexCount = 0;
	land->centre.x = 0;
	land->centre.y = 0;
	int ii = 0;
	
	while (fscanf(input, "%lf %lf\n", &land->vertex[ii].x, 
		&land->vertex[ii].y) == 2)
	{
		ii++;
	}
	land->vertexCount = ii;
	//printf("land vertex count: %d\n", land->vertexCount);
	createEdges(land);
}

void genAsteroid(struct Environment *env)
{
	struct Asteroid ast;
	ast.exists = 1;
	int border;
	border = randInt(2);
	if (border == 0)
	{
		ast.loc.centre.y = 0;
		ast.loc.centre.x = randInt(635);
		ast.kin.yVel = 70;
		ast.kin.xVel = randInt(40);
	}
	else if (border == 1)
	{
		ast.loc.centre.x = 0;
		ast.loc.centre.y = randInt(635); // need to know
		ast.kin.xVel = 70;
		ast.kin.yVel = randInt(40);
	}
	else if (border == 2)
	{
		ast.loc.centre.x = 635;
		ast.loc.centre.y = randInt(635); // need to know
		ast.kin.xVel = -70;
		ast.kin.xVel = randInt(40);
	}
	
	env->asteroid = ast;
}

int detectCollision(struct Location *ship, struct Location *land)
{
	for (int ii = 0; ii < ship->vertexCount; ii++)
	{
		for (int jj = 0; jj < land->vertexCount; jj++)
		{
			if (detectIntersection(&(ship->edge[ii]), 
				&(land->edge[jj]), &(ship->centre)))
			{
				//ship->impactEdge = ii;
				land->intersectedEdge = jj;
				return 1;
			}
		}
	}
	return 0;
}

int isFlat(struct Location *land)
{
	double y1 = land->edge[land->intersectedEdge].pointA.y;
	double y2 = land->edge[land->intersectedEdge].pointB.y;
	if (areEqualFloats(y1,y2))
		return 1;
	return 0;
}
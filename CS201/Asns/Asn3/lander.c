/* name:               		Mark Tupala
ONE Card number:    	1188594
Unix id:            		tupala
lecture section:    		B1
instructor's name:  		Dr. Martin Muller
lab section:        		H02
TA's name:          		Aditya Bhargava
*/

/* 
Reads each line of an input file given as an argument,
and takes the appropriate action based on the type of line,
including sending commands to Sketchpad.jar, storing data
in memory, and printing to stdout.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <unistd.h>

#include "utilities.h"
#include "realtime.h"
#include "keyboard.h"
#include "landscape.h"
#include "spaceship.h"
#include "sketchpad.h"
#include "physics.h"

#define NUM_ARGS 6
#define ANGLE_MAG 10

// Global variables:
// name of the program being run, from argv[0]
char progName[MAX_FILENAME_LEN + 1];
// name of input file being given as argument, from argv[1]
char inputName[MAX_FILENAME_LEN + 1];
// name of the program to which information is sent.
const char execName[] = "java -jar Sketchpad.jar";



// responsible for opening input file and pipe, calling
// storeLand() with those arguments, and returning successfully
int main(int argc, char *argv[])
{
	char ans;
	float gravity, thrust;
	int fuelOn = 0;
	// store names of program and input file in globals from utilities.h
	memset(progName, 0, MAX_FILENAME_LEN + 1);
	strncpy(progName, argv[0], MAX_FILENAME_LEN + 1);
	//memset(inputName, 0, MAX_FILENAME_LEN + 1);
	//strncpy(inputName, argv[1], MAX_FILENAME_LEN + 1);
	
	// check for correct number of arguments
	//~ if (argc != NUM_ARGS + 1)
	//~ {
		//~ reportError();
		//~ exit(EXIT_FAILURE);
	//~ }
	// assign default funcs here, only overwrite if -i found
	void (*thrustFunc) (struct spaceship *);
	thrustFunc = accelShip;
	for (int ii = 1; ii < argc; ii++)
	{
		if (strncmp(argv[ii], "-g", 2) == 0)
			gravity = strtof(argv[ii + 1], NULL);
		else if (strncmp(argv[ii], "-t", 2) == 0)
			thrust = strtof(argv[ii + 1], NULL);
		else if (strncmp(argv[ii], "-f", 2) == 0)
			strcpy(inputName, argv[ii + 1]);
		else if (strncmp(argv[ii], "-i", 2) == 0)
		{
			fuelOn = 1;
			thrustFunc = accelShipWithFuel;
		}
	}
	//printf("gravity: %f\n", gravity);
	//printf("thrust: %f\n", thrust);
	
	// open file
	inputfile = fopen(inputName, "r");
	if (inputfile == NULL)
	{
		reportError();
		exit(EXIT_FAILURE);
	}
	
	// open pipe
	exec = popen(execName, "w");
	if (exec == NULL)
		funcError("Could not open pipe", execName);
	
	storeLand(&land, inputfile);
	createShip(&ship, thrust, gravity);

	// start curses
	startCurses();
	changeImage(&land, 'D');
	changeImage(&ship.loc, 'D');
	// IMPROVEMENT
	if (fuelOn)
		createFuel(ship.fuel);
	// start signal
	//sigset_t old_mask;
	struct itimerval myTimer;
	createSignal(&myTimer);
	
	while (1)
	{
		// get response from player
		ans = runCurses();
		
		shieldUp();
		if (ans == 'Q')
		{
			myTimer.it_interval.tv_usec = 0;
			myTimer.it_value.tv_usec = 0;
			gameOver("Quitting");
		}
		else if (ans == 'L')
			rotateShip(&ship, -ANGLE_MAG);
		else if (ans == 'R')
			rotateShip(&ship, ANGLE_MAG);
		else if (ans == 'S')
			thrustFunc(&ship);
		shieldDown();
	}
}	






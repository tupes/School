/* name:               		Mark Tupala
ONE Card number:    	1188594
Unix id:            		tupala
lecture section:    		B1
instructor's name:  		Dr. Martin Muller
lab section:        		H02
TA's name:          		Aditya Bhargava
*/

#ifndef TIMER_H
#define TIMER_H

// need to define this macro as functions we're using are not C99
// compliant
#define _POSIX_C_SOURCE 200112L

// must include these 2 header files
#include <signal.h>
#include <sys/time.h>

#include <stdio.h>
#include <stdlib.h>

#include "spaceship.h"

#define SECONDARY_TIMER 100

// will store alarm signal to indicate we want it blocked
sigset_t block_mask_g;
sigset_t old_mask;

// our function which we will have called whenever the timer expires
void createSignal(struct itimerval *myTimer);
void applyTime(int signal);
void applyTimeWithSecondary(int signal);
void shieldUp();
void shieldDown();

#endif
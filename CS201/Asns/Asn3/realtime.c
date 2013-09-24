/* name:               		Mark Tupala
ONE Card number:    	1188594
Unix id:            		tupala
lecture section:    		B1
instructor's name:  		Dr. Martin Muller
lab section:        		H02
TA's name:          		Aditya Bhargava
*/

// Illustrates how to use a timer to print something every x seconds,
// and how to block code from being interrupted by this timer

#include "realtime.h"

void createSignal(struct itimerval *myTimer)
{
	// blocking
	sigemptyset(&block_mask_g); 
	sigaddset(&block_mask_g, SIGALRM);
	// handler
	struct sigaction handler;
	// DETERMINED BY ASTEROIDS OR NOT
	handler.sa_handler = applyTimeWithSecondary;
	sigemptyset(&handler.sa_mask);
	handler.sa_flags = 0;

	if (sigaction(SIGALRM, &handler, NULL) == -1)
		exit(EXIT_FAILURE);
	// timer
	struct itimerval timer;
	struct timeval time_delay;
	time_delay.tv_sec = 0;
	time_delay.tv_usec = 50000;
	timer.it_interval = time_delay;
	struct timeval start;
	start.tv_sec = 1;
	start.tv_usec = 50000;
	timer.it_value = start;
	
	if (setitimer(ITIMER_REAL, &timer, NULL) == -1)
		exit(EXIT_FAILURE);
	*myTimer = timer;
}

void shieldUp()
{
	if (sigprocmask(SIG_BLOCK, &block_mask_g, &old_mask) < 0)
		exit(EXIT_FAILURE);
}

void shieldDown()
{
	if (sigprocmask(SIG_SETMASK, &old_mask, NULL) < 0)
		exit(EXIT_FAILURE);
}

// called when SIGALRM is sent.
void applyTime(int signal)
{
	static int called = 0;

	// called because of SIGALRM
	if (signal == SIGALRM)
	{
		called++;
		// gets timer, puts it into timer (man 2 getitimer)
		struct itimerval timer;
		if (getitimer(ITIMER_REAL, &timer) == -1)
			exit(EXIT_FAILURE);

		// call critical code
		shieldUp();
		execCritical();
		shieldDown();
		// end critical code

		if (setitimer(ITIMER_REAL, &timer, NULL) == -1)
			exit(EXIT_FAILURE);
	}
}

void applyTimeWithSecondary(int signal)
{
	static int called = 0;
	// called because of SIGALRM
	if (signal == SIGALRM)
	{
		called++;
		
		// gets timer, puts it into timer (man 2 getitimer)
		struct itimerval timer;
		if (getitimer(ITIMER_REAL, &timer) == -1)
			exit(EXIT_FAILURE);

		// call critical code
		shieldUp();
		execCritical_2();
		if (called == SECONDARY_TIMER)
		{
			execCriticalSecondary();
			called = 0;
		}
		shieldDown();
		// end critical code

		if (setitimer(ITIMER_REAL, &timer, NULL) == -1)
			exit(EXIT_FAILURE);
	}
}

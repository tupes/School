/* name:               		Mark Tupala
ONE Card number:    	1188594
Unix id:            		tupala
lecture section:    		B1
instructor's name:  		Dr. Martin Muller
lab section:        		H02
TA's name:          		Aditya Bhargava
*/


//#include <stdio.h>
//#include <stdlib.h>
#include "keyboard.h"

// brief example of using curses.
// man 3 ncurses for introductory man page, and man 3 function name
// for more information on that function.

void startCurses()
{
	int c;
	setup_curses();
	move(5, 10);
	printw("Press any key to start.");
	move(6, 10);
	printw("(Then press arrow keys to rotate, space for thrust, 'q' to quit.)");
	refresh();
	c = getch();
}

void printOutcome(char msg)
{
	int c;
	move(7, 15);
	if (msg == 'L')
		printw("LANDED!!!!");
	else if (msg == 'C')
		printw("CRASH!!!");
	refresh();
	while (1)
	{
		c = getch();
		if (c == 'q')
			break;
	}
}

char runCurses()
{
    int c = getch();

    if (c != ERR)
    {
      if (c == KEY_LEFT)
        return 'L';
      else if (c == KEY_RIGHT) 
        return 'R';
      else if (c == ' ') 
        return 'S';
      else if (c == 'q')
        return 'Q';
    }
    return 'N';
}

void setup_curses()
{
  // use return values.  see man pages.  likely just useful for error
  // checking (NULL or non-NULL, at least for init_scr)
  initscr();
  cbreak();
  noecho();
  // needed for cursor keys (even though says keypad)
  keypad(stdscr, true);
}

void unset_curses()
{
  keypad(stdscr, false);
  nodelay(stdscr, false);
  nocbreak();
  echo();
  endwin();
}

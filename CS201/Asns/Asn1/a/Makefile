# name:               Mark Tupala
# ONE Card number:    1188594
# Unix id:            tupala
# lecture section:    B1
# instructor's name:  Dr. Martin Muller
# lab section:        H02
# TA's name:          Aditya Bhargava
#
# Creates a draw1a executable, and provides a make clean.
#

draw1a: draw1a.o
	gcc -Wall -std=c99 -o draw1a draw1a.o -lm

draw1a.o: draw1a.c draw1a.h
	gcc -Wall -std=c99 -c draw1a.c

clean:
	-rm -f *.o draw1a core

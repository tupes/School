# name:               Mark Tupala
# ONE Card number:    1188594
# Unix id:            tupala
# lecture section:    B1
# instructor's name:  Dr. Martin Muller
# lab section:        H02
# TA's name:          Aditya Bhargava
#
# Creates a draw1b executable, and provides a make clean.
# Compile by typing: make
# Delete executable and all .o files by typing: make clean
#

draw1b: draw1b.o
	gcc -Wall -std=c99 -o draw1b draw1b.o -lm

draw1b.o: draw1b.c draw1b.h
	gcc -Wall -std=c99 -c draw1b.c

clean:
	-rm -f *.o draw1b core

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

draw2: draw2.o memwatch.o matrix.o sketchpad.o utilities.o parse.o 
	gcc -Wall -std=c99 -o draw2 draw2.o memwatch.o matrix.o sketchpad.o \
utilities.o parse.o -lm -g

draw2.o: draw2.c memwatch.h parse.c matrix.c sketchpad.c utilities.c parse.h \
matrix.h sketchpad.h utilities.h
	gcc -Wall -std=c99 -DMEMWATCH -DMW_STDIO -c draw2.c -g 

parse.o: parse.c parse.h memwatch.h matrix.c sketchpad.c utilities.c matrix.h \
sketchpad.h utilities.h
	gcc -Wall -std=c99 -DMEMWATCH -DMW_STDIO -c parse.c -lm -g

matrix.o: matrix.c matrix.h memwatch.h sketchpad.c utilities.c parse.c \
sketchpad.h utilities.h parse.h
	gcc -Wall -std=c99 -DMEMWATCH -DMW_STDIO -c matrix.c -lm -g

sketchpad.o: sketchpad.c sketchpad.h memwatch.h matrix.c utilities.c parse.c \
matrix.h utilities.h parse.h
	gcc -Wall -std=c99 -DMEMWATCH -DMW_STDIO -c sketchpad.c -lm -g

utilities.o: utilities.c utilities.h memwatch.h sketchpad.c sketchpad.h
	gcc -Wall -std=c99 -DMEMWATCH -DMW_STDIO -c utilities.c -lm -g

clean:
	-rm -f *.o draw2 core

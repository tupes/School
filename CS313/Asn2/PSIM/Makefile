psim: asn2.o sim.o
	gcc -Wall -std=c99 -o psim asn2.o sim.o -lm

asn2.o: asn2.c sim.c sim.h que.c que.h
	gcc -Wall -std=c99 -c asn2.c -lm

sim.o: sim.c sim.h que.c que.h
	gcc -Wall -std=c99 -c sim.c -lm

clean:
	-rm -f *.o esim core

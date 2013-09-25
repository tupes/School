
esim: asn1.o network_sim.o
	gcc -Wall -std=c99 -o esim asn1.o network_sim.o -lm

asn1.o: asn1.c network_sim.c network_sim.h
	gcc -Wall -std=c99 -c asn1.c -lm

network_sim.o: network_sim.c network_sim.h
	gcc -Wall -std=c99 -c network_sim.c -lm

clean:
	-rm -f *.o esim core

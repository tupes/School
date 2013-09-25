
#include "sim.h"


int main (int argc, char *argv[])
{
    char* protocol = argv[1];
    int N = atoi(argv[2]);
    float p = atof(argv[3]);
    int R = atoi(argv[4]);
    int T = atoi(argv[5]);
    
    run(protocol, N, p, R, T);
    
    //~ out = open('asn2_results.txt', 'a')
    //~ output(out, stations, protocol, N, p, R, T)
    //~ out.close()
	

	return 0;
}

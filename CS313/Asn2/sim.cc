#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;


class Station {
	int* num_stations,* number;
	float* prob;
	public:
		Station (int, float, int);
		~Station();
};

Station::Station (int number_stations, float gen_prob, int n) {
	num_stations = new int;
	prob = new float;
	number = new int;
	int* frames_sent = new int;
	int* delay = new int;
	
	*num_stations = number_stations;
	*prob = gen_prob;
	*number = n;
	*frames_sent = 0;
	*delay = 0;
}

Station::~Station() {
	delete num_stations;
	delete number;
	delete prob;
}

// start simulation
Station* run(string protocol, int num_stations, float prob, 
					int num_slots, int num_trials) {
    Station* stations;
	if (protocol == "P") {
		
		for (int n = 0; n < num_stations; n++) {
			stations[n] = new Station (num_stations, prob, n);
		}
        //~ stations = [P_Station(num_stations, prob, n) for n in range(num_stations)]
    //~ elif protocol == 'I':
        //~ stations = [I_Station(num_stations, prob, n) for n in range(num_stations)]
    //~ elif protocol == 'B':
        //~ stations = [B_Station(num_stations, prob, n) for n in range(num_stations)]
    //~ elif protocol == 'T':
        //~ stations = [T_Station(num_stations, prob, n) for n in range(num_stations)]
    //~ else:
        //~ print 'unknown protocol'
        //~ exit()
    //~ for trial in range(num_trials):
        //~ run_trial(stations, params)
        //~ store_trial(stations)
    //~ produce_results(stations, params)
	}
    return stations;
}
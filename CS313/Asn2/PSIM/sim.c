
#include "sim.h"
#include "que.c"

struct Param param;

struct Station* get_stations(int num_stations) {
	struct Station* stations[num_stations];
	for (int n = 0; n < num_stations; n++)
		stations[n] = malloc(sizeof(struct Station));
	return stations[0];
}

// start simulation
void run(char* protocol, int num_stations, float prob, 
					int num_slots, int num_trials) {

	struct Station* stations = get_stations(num_stations);
	param.protocol = *protocol; printf("%c\n", param.protocol);
	param.num_stations = num_stations; printf("%i\n", param.num_stations);
	param.prob = prob; printf("%f\n", param.prob);
	param.num_slots = num_slots; printf("%i\n", param.num_slots);
	param.num_trials = num_trials; printf("%i\n", param.num_trials);
	
	// determine station behaviour based on protocol
	if (*protocol == 'P') {
		param.check_attempt = P_check_attempt;
		param.collide = P_collide; 
	}
	else if (*protocol == 'I') {
		param.check_attempt = default_check_attempt;
		param.collide = I_collide; 
	}
	else if (*protocol == 'B') {
		param.check_attempt = default_check_attempt;
		param.collide = B_collide; 
	}
	else if (*protocol == 'T') {
		param.check_attempt = T_check_attempt;
	}
	
	// initialize stations
	for (int n = 0; n < num_stations; n++) {
		stations[n].protocol = *protocol; 
		stations[n].num_stations = num_stations; 
		stations[n].prob = prob; 
		stations[n].number = n; 
		stations[n].frames_sent = 0; 
		stations[n].delay = 0; 
		stations[n].collisions = 0;
		if (*protocol == 'T')
			stations[n].counter = n;
		else
			stations[n].counter = 0;
	}

	// run trials
    for (int trial = 0; trial < num_trials; trial++) {
        run_trial(param, stations);
		printf("finished trial %d\n", trial);
        //store_trial(stations);
    //produce_results(stations, param);
	}
    //return stations;
}

// done
void run_trial(struct Param param, struct Station *stations) {
	struct Station* attempting[param.num_stations];
	for (int station = 0; station < param.num_stations; station++) {
		stations[station].que = create_que();
	}
	puts("finished creating ques");
    for (int slot = 0; slot < param.num_slots; slot++) {
        for (int station = 0; station < param.num_stations; station++) {
            do_slot(param, stations[station], attempting);
			
		}
		puts("finished updating stations");
        transmit_frame(param, attempting);
		puts("finished transmitting");
	}
}

// done
void do_slot(struct Param param, struct Station station, struct Station* attempting[]) {
	int must_attempt = 0;
	if (get_random() < station.prob) {
		must_attempt = create_frame(&station);
	}
	increment_delays(station.que);
	int will_attempt = (param.check_attempt) (&station);
	if (!is_empty(station.que) && (must_attempt || will_attempt))
		attempting[station.number] = &station;
	else
		attempting[station.number] = NULL;
}

// done
int create_frame(struct Station* station) {
	//puts("creating frame");
	struct node *node;
	node = create_node(1);
	int must_attempt;
	if (is_empty(station->que))
		must_attempt = 1;
	else
		must_attempt = 0;
	enqueue(station->que, node);
	return must_attempt;
}

// done
void increment_delays(struct que* que) {
	for (struct node* node = que->head; node != NULL; node = node->next)
		node->value += 1;
}

// done
void transmit_frame(struct Param param, struct Station* attempting[]) {
	int num_attempting = get_attempting(param, attempting);
	printf("%d stations wish to transmit\n", num_attempting);
	if (num_attempting == 1)
		transmit(get_station(param, attempting));
	else if (num_attempting > 1) {
		for (int n = 0; n < param.num_stations; n++) {
			if (attempting[n] != NULL)
				param.collide(attempting[n]);
		}
	}
}

// done
int get_attempting(struct Param param, struct Station* attempting[]) {
	int found = 0;
	for (int n = 0; n < param.num_stations; n++) {
		if (attempting[n] != NULL)
			found += 1;
	}
	return found;
}

// done
struct Station* get_station(struct Param param, struct Station* attempting[]) {
	for (int n = 0; n < param.num_stations; n++) {
		if (attempting[n] != NULL)
			return attempting[n];
	}
	return NULL;
}

// done
int P_check_attempt(struct Station* station) {
	//puts("P check");
	if (get_random() < 1.00 / station->num_stations)
		return 1;
	else
		return 0;
}

// done
int T_check_attempt(struct Station* station) {
	//puts("T check");
	if (station->counter) {
		station->counter -= 1;
		return 0;
	}
	else {
		station->counter = station->num_stations - 1;
		return 1;
	}
}

// done
int default_check_attempt(struct Station* station) {
	//puts("default check");
	if (station->counter) {
		station->counter -= 1;
		return 0;
	}
	else {
		return 1;
	}
}

// done
void P_collide(struct Station* station) {
	;
}

// done
void I_collide(struct Station* station) {
	station->counter = get_int(station->num_stations - 1);
}

// done
void B_collide(struct Station* station) {
	if (station->collisions < 10)
		station->collisions += 1;
	station->counter = get_int(pow(2.0, (double) station->collisions) - 1);
}

// done
void transmit(struct Station* station) {
	//puts("transmit");
	station->delay += dequeue(station->que);
	station->frames_sent += 1;
	station->collisions = 0;
}

double get_random() {
	double num = drand48(); printf("random number is %lf\n", num); return num;
	//return drand48();
}

int get_int(int max_int) {
	return  (int) floor( (max_int + 1)  * get_random());
}
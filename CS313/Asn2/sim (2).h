
#ifndef NETSIM_H
#define NETSIM_H

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

extern struct Station {
	char protocol;
	int num_stations;
	float prob;
	int number;
	int frames_sent;
	int delay;
	int counter;
	int collisions;
	struct que *que;
};

extern struct Param {
	char protocol;
	int num_stations;
	float prob;
	int num_slots;
	int num_trials;
	int (*check_attempt) (struct Station* station);
	void (*collide) (struct Station* station);
};

struct Station* get_stations(int num_stations);
void run_trial(struct Param params, struct Station *stations);
void do_slot(struct Param param, struct Station station, struct Station* attempting[]);
int create_frame(struct Station* station);
void increment_delays(struct que* que);
void transmit_frame(struct Param param, struct Station* attempting[]);
int get_attempting(struct Param param, struct Station* attempting[]);
struct Station* get_station(struct Param param, struct Station* attempting[]);

//~ extern struct node {
	//~ int delay;
	//~ struct node *next;
//~ };

//~ extern struct Que {
	//~ struct node *head;
	//~ struct node *tail;
	//~ long count;
//~ };

//~ int is_empty(struct Que* que);

void run(char* protocol, int num_stations, float prob, 
					int num_slots, int num_trials);

int P_check_attempt(struct Station* station);
int T_check_attempt(struct Station* station);
int default_check_attempt(struct Station* station);

void P_collide(struct Station* station);
void I_collide(struct Station* station);
void B_collide(struct Station* station);

void transmit(struct Station* station);

double get_random();
int get_int(int max_int);
void srand48(int);
double drand48(void);
//double pow(double, double);
//double floor(double);
#endif
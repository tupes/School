
#ifndef NETSIM_H
#define NETSIM_H

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

extern long attempts;
extern long correct_frames;
extern long total_time;
extern long seed_index;

int get_checkbits(int data_bits);

void run_trials(int T, int R, int num_blocks, int block_size, int A, double e, int max_errors, char *argv[]);

int run_trial(int R, int num_blocks, int block_size, int A, double e, int max_errors);

int send_frame(int num_blocks, int block_size, int A, double e, int max_errors);

int send_blocks(int num_blocks, int block_size, double e, int max_errors);

int send_block(int block_size, double e, int max_errors);

void set_seed(char *seed_string);

double get_random(void);

void srand48(int);
double drand48(void);

#endif
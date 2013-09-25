
#include "network_sim.h"

long attempts = 0;
long correct_frames = 0;
long total_time = 0;
long seed_index = 7;


int get_checkbits(int data_bits) {
	int check_bits = 3;
	int m = 4;
	while (m < data_bits) {
		check_bits += 1;
		m *= 2;
		
	}
	return check_bits;
}


void run_trials(int T, int R, int num_blocks, int block_size, int A, double e, int max_errors, char *argv[]) {
	for (int trial = 0; trial < T; trial++) {
		set_seed(argv[seed_index]);
		total_time += run_trial(R, num_blocks, block_size, A, e, max_errors);
	}
}


int run_trial(int R, int num_blocks, int block_size, int A, double e, int max_errors) {
	int trial_time = 0;
	while (trial_time < R) {
		trial_time += send_frame(num_blocks, block_size, A, e, max_errors);
		correct_frames += 1;
	}
	return trial_time;
}


int send_frame(int num_blocks, int block_size, int A, double e, int max_errors) {
	int frame_time = 0;
	int frame_success = 0;
	while (!frame_success) {
		frame_success = send_blocks(num_blocks, block_size, e, max_errors);
		frame_time += (num_blocks * block_size) + A;
		attempts += 1;
	}
	return frame_time;
}


int send_blocks(int num_blocks, int block_size, double e, int max_errors) {
	int blocks_success = 1;
	for (int block = 0; block < num_blocks; block++) {
		if (!send_block(block_size, e, max_errors))
			blocks_success = 0;
	}
	return blocks_success;
}
	

int send_block(int block_size, double e, int max_errors) {
	int errors = 0;
	for (int bit = 0; bit < block_size; bit++) {
		if (get_random() < e)
			errors += 1;
	}
	if (errors > max_errors) return 0;
	return 1;
}


void set_seed(char *seed_string) {
	srand48(atoi(seed_string));
	seed_index += 1;
}

double get_random() {
	return drand48();
}

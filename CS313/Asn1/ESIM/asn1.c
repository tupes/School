
#include "network_sim.h"

const char file_name[] = "asn1_sim_results.txt";

int main(int argc, char *argv[]) {
	int A = atoi(argv[1]); // feedback time
	int K = atoi(argv[2]); // number of blocks
	int F = atoi(argv[3]); // size of frame in bits
	double e = atof(argv[4]); // error probability rate
	int R = atoi(argv[5]); // duration of simulation
	int T = atoi(argv[6]); // number of trials
	
	double data_bits;
	int num_blocks, block_size, r, max_errors;
	
	// open file for writing results
	FILE *results_file = fopen(file_name, "a");
	if (results_file == NULL)
		exit(EXIT_FAILURE);
	
	// check if K is the special case 0
	if (K) { 
		data_bits = F / K;
		r = get_checkbits(data_bits);
		max_errors = 1;
		num_blocks = K;
	} else {
		data_bits = F;
		r = 0;
		max_errors = 0;
		num_blocks = 1;
	}
	block_size = data_bits + r;
	
	// run sim
	run_trials(T, R, num_blocks, block_size, A, e, max_errors, argv);
	
	// calculate results
	double avg_frame_trans = attempts / (double) correct_frames;
	double throughput = (F * correct_frames) / (double) total_time;
	
	// write results
	for (int arg = 0; arg < argc; arg++) {
		fputs(argv[arg], results_file);
		fprintf(results_file, " ");
	}
	fprintf(results_file, "\n");
	fprintf(results_file, "%lf\n", avg_frame_trans);
	fprintf(results_file, "%lf\n", throughput);
	fclose(results_file);

}

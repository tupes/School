from sys import argv
import random

def get_checkbits(data_bits):
	check_bits = 3;
	m = 4;
	while m < data_bits:
		check_bits += 1;
		m *= 2;
	return check_bits;

def run_trials():
	global total_time;
	for trial in range(T):
		total_time += run_trial();

def run_trial():
	#print 'running trial'
	trial_time = 0;
	set_seed();
	global correct_frames;
	while trial_time < R:
		trial_time += send_frame();
		correct_frames += 1;
	#print 'finished trial'
	return trial_time;

def send_frame():
	frame_time = 0;
	global attempts;
	success = False;
	while not success:
		block_failed = False;
		for block in range(num_blocks):
			if not send_block():
				block_failed = True;
			frame_time += block_size;
		frame_time += A;
		attempts += 1;
		if not block_failed: success = True;
	return frame_time;	

def send_block():
	errors = 0;
	for bit in range(block_size):
		if get_random() < e:
			errors += 1;
	if errors > max_errors: return False;
	return True;

# output funcs

def get_avg_frame_trans(frame_trans, correct_frames):
	#show(frame_trans, correct_frames)
	return frame_trans / float(correct_frames);

def get_throughput(F, correct_frames, total_time):
	#show(correct_frames, total_time)
	return (F * correct_frames) / float(total_time);

def show(*args):
	for arg in args: print arg

def write_results():
	f = open('results_K0.txt', 'a')
	f.write(' '.join(argv) + '\n')
	f.write(str(avg_frame_trans) + '\n')
	f.write(str(throughput) + '\n')
	f.close()

# python specific
def set_seed():
	global x
	random.seed(seeds[x])
	x += 1
	
def get_seeds():
	return [random.seed(x) for x in [50, 100, 150, 200, 250]]

def get_random():
	return random.random()

if __name__ == '__main__':
	# input parameters
	A = int(argv[1]); # feedback time
	K = int(argv[2]); # number of blocks
	F = int(argv[3]); # size of frame in bits
	e = float(argv[4]); # error probability rate
	R = int(argv[5]); # duration of simulation
	T = int(argv[6]); # number of trials
	
	x = 0
	seeds = [50, 100, 150, 200, 250]
	
	if K: 
		data_bits = F / K;
		r = get_checkbits(data_bits);
		max_errors = 1;
		num_blocks = K;
	else:
		data_bits = F;
		r = 0;
		max_errors = 0;
		num_blocks = 1;
	assert data_bits % 1 == 0;
	block_size = data_bits + r;
	attempts = 0;
	correct_frames = 0;
	total_time = 0;
	run_trials();

	# output
	avg_frame_trans = get_avg_frame_trans(attempts, correct_frames);
	throughput = get_throughput(F, correct_frames, total_time);
	#show(A, K, F, e, R, T, avg_frame_trans, throughput);
	write_results();

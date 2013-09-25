from sys import argv
from sim import run

def main():
    protocol = argv[1]
    N = int(argv[2])
    p = float(argv[3])
    R = int(argv[4])
    T = int(argv[5])
    seeds = [int(arg) for arg in argv[6:]]
    
    stations = run(protocol, N, p, R, T, seeds)
    
    out = open('results/' + protocol + '_asn2_results.txt', 'a')
    output(out, stations, protocol, N, p, R, T)
    out.close()

def output(out, stations, protocol, N, p, R, T):
    line1(out, protocol, N, p, R, T)
    total_slots = T * R
    total_frames = total_delay = 0
    for station in stations:
        total_frames += station.frames_sent
        total_delay += station.delay
    line2(out, T, R, total_frames, total_slots)
    line3(out, total_delay, total_frames)
    node_lines(out, stations, total_slots)

def line1(out, protocol, N, p, R, T):
    line = ' '.join([str(arg) for arg in [protocol, N, p, R, T]])
    produce(out, line)

def line2(out, T, R, total_frames, total_slots):
    throughput = total_frames / float(total_slots)
    produce(out, str(throughput))

def line3(out, total_delay, total_frames):
    delay = total_delay / float(total_frames)
    produce(out, str(delay))

def node_lines(out, stations, total_slots):
    for station in stations: produce(out, station.get_results(total_slots))

def produce(out, line):
    print line
    out.write(line + '\n')


if __name__ == '__main__':
    main()


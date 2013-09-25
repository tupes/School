import subprocess

min_prob = 0.001
max_prob = 0.04000001
prob_step = 0.001

seeds = [100, 200, 300, 400, 500]

for proto in ['P', 'I', 'B', 'T']:
    print 'running', proto
    prob = min_prob
    while prob < max_prob:
        subprocess.call(["./psim.py", proto, "20", str(prob), "50000", "5", 
		str(seeds[0]), str(seeds[1]), str(seeds[2]), str(seeds[3]), str(seeds[4])])

        print 'finished prob', prob
        prob += prob_step

print 'finished sim'
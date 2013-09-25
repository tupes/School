
k_index = 2
e_index = 4

out = open('formatted.txt', 'w')
data = open('asn1_sim_results.txt')
lines = data.readlines()
data.close()

sep = '\t'

i = counter = 0
while i < len(lines):
    tokens = lines[i].split()
    k_val = tokens[k_index]
    e_val = tokens[e_index]
    i += 1 # switch between avg frames and throughput
    val = lines[i].strip()
    out.write(val + sep)
    i += 2 # switch between avg frames and throughput
    counter += 1
    if counter == 10:
        counter = 0
        out.write('\n')
    
out.close()
import subprocess

seeds[] = [50, 100, 150, 200, 250]

min_e = 0.0
max_e = 0.002
e_step = 0.0001

for K in range(1):
	e = min_e
	while e <= max_e:
		#args = "asn1.py 100 " + str(K) + " 8000 " + str(e) + " 8000000 5"
		subprocess.call(["python", "asn1_2.py", "100", str(K), "8000", str(e), "80000000", 
				"5", str(seeds[0]), str(seeds[1]), str(seeds[2]), str(seeds[3]), str(seeds[4])])
		print 'finished', K, e		
		e += e_step
		

print 'finished sim'

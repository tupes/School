import math
import random
import sys

def p8(n):
		poisoned = random.randint(0, n - 1)
		cups = [x for x in range(n)]
		sq = int(math.sqrt(n)); print sq
		peons = []
		first = 0
		last = sq
		while first < n - 1:
			peons.append(cups[first:last])
			first = last
			last += sq
		for x in range(sq):
			temp = []
			for y in cups[x::sq]:
				temp.append(y)
			peons.append(temp)
		
		print peons
		
		print 'Number of tasters:', len(peons)
		logn = math.log(n, 2)
		print 'Log n:', logn
		if len(peons) <= logn: print 'Success!'
		else: print 'Failure!'


n = int(sys.argv[1])
p8(n)
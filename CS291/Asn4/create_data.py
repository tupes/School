from sys import argv
from string import lowercase
from random import choice

if __name__ == '__main__':
	output = open('../data/'+'_'.join(argv[1:]), 'w')
	scores = [str(x) for x in range(11)]
	raters = [''.join([choice(lowercase) for x in range(10)]) for rater in range(int(argv[2]))]
	for x in range(int(argv[1])):
		output.write('{['+str(x)+'],[title],[artist],[' + ','.join(['('+choice(raters)+','+choice(scores)+')' for y in range(int(argv[3]))]) + ']}\n')
	output.close()
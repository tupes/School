
import sys
from numpy import *
from pylab import *

def main(filename):
    #filename = sys.argv[1]
    data = loadtxt(filename)
    plot(data)
    xlabel('episodes')
    ylabel('total steps')
    ylim([0, 800])

    

if __name__ == '__main__':
   main('F:/school/cs/366/projects/proj3/results.txt')
   show()
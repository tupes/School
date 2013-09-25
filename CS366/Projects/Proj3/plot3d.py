'''
Created on Nov 17, 2011

@author: rupam
'''
import sys
import csv
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

path = 'F:/school/cs/366/projects/proj3/matrix.csv'

def main():
    x1steps = 50 #int(sys.argv[4])
    x2steps = 50 #int(sys.argv[7])
    x1range = linspace(-1.2, 0.5, x1steps)
    x2range = linspace(-0.07, 0.07, x2steps)
    cr = csv.reader(open(path, 'rt'), delimiter=',', quotechar='|')
    data = []
    i = 0
    for row in cr:                                                      
        data.append(row)
        i+=1
    i = 0
    for lst in data:
        j = 0
        for value in lst:
            if value!='':
                data[i][j] = float(value)
            else:
                data[i].remove('')
            j+=1
        i+=1 

    y = array(data)
	
    fig = figure()
    ax = Axes3D(fig)
    x1,x2 = meshgrid(x1range,x2range)
    ax.plot_surface(x1, x2, y.T, cstride=1, rstride=1, cmap=cm.jet)
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')
    ax.set_zlabel('$y$')
    #savefig("plot.pdf")
    
if __name__ == '__main__':
    main()
    show()

from pylab import *
from mpl_toolkits.mplot3d import Axes3D
#from numpy import array

def get_data(lines):
    i = 0
    data = list()
    while i < len(lines):
        data.append(list())
        params = lines[i].split()
        k_val = int(params[2])
        e_val = float(params[4])
        #if kval > 20: break
        k.append(k_val)
        e.append(e_val)
        i += 1
        y.append(float(lines[i].strip()))
        i += 2

def show_points(k, e, y):
    assert len(k) == len(e) == len(y)
    for i in range(len(k)):
        print k[i], e[i], y[i] 

def main():
    
    f = open('results.txt')
    lines = f.readlines()
    f.close()
    get_data(lines)
    
    #show_points(k, e, y)
    y = array(data)
    fig = figure()
    ax = Axes3D(fig)
#    x1steps = 50 #int(sys.argv[4])
#    x2steps = 50 #int(sys.argv[7])
#    x1range = linspace(0, 1000, x1steps)
#    x2range = linspace(0.0, 0.001, x2steps)
#    x1,x2 = meshgrid(x1range,x2range)
    #ax.scatter(k, e, y)    
    ax.plot_surface(k, e, y, cmap=cm.jet)#, cstride=1, rstride=1, cmap=cm.jet)
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')
    ax.set_zlabel('$y$')
    #savefig("plot.pdf")
    
if __name__ == '__main__':
    main()
    show()
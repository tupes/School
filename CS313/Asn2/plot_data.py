import matplotlib.pyplot as plt

def make_graph(info, proto):
    f = open('results/' + proto + '_asn2_results.txt')
    lines = f.readlines()
    f.close()
    if info == 'through': 
        step = 1
        max_y = 0.2
    elif info == 'delay': 
        step = 2
        max_y = 100
    else: print 'wrong type of info'; exit()
    data = get_data(lines, step, proto)
    print data
    show(data, max_y, proto)


def get_data(lines, step, proto):
    data = list()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith(proto):
            i += step
            data.append(float(lines[i]))
        i += 1
    return data
        
    
def show(data, max_y, proto):
    min_x = 0.001
    step = 0.001
    line = plt.plot([min_x + (step * i) for i in range(len(data))], data)
    #plt.axis([min_x, max_x, 0, max_y])
    plt.axis(ymax = max_y)
    plt.setp(line, label = proto)
    print plt.axis()
    


if __name__ == '__main__':
    #info = 'delay'
    info = 'through'
    for proto in ['P', 'I', 'B', 'T']:
        make_graph(info, proto)
    #plt.legend(loc = 'upper right')
    plt.legend(loc = 'upper left')
    plt.xlabel('Frame Generation Probability')
    #plt.ylabel('Average Delay in Slots')
    plt.ylabel('Average Throughput')
    #plt.title('Average Delay of Protocols')
    plt.title('Average Throughput of Protocols')
    plt.show()

def centroid(X,Y):
    '''Returns the centroid x and y of the supplied coordinates'''
    x = 0
    y = 0
    length = len(X)
    for i in range(length):
        x += X[i]
        y += Y[i]
    return (x/length,y/length)

from math import sqrt
def distance(x1,y1,x2,y2):
    '''Returns the distance between two points'''
    return sqrt((x2-x1)**2 + (y2-y1)**2)


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    plt.scatter([1,2,3],[0,3,0])
    x,y = centroid([1,2,3],[0,3,0])
    plt.scatter(x,y)
    plt.show()

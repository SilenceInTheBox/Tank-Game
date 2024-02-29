import random as r
import matplotlib.pyplot as plt

'''Terrain Generator v 0.1
        Creates list containing coordinates for randomly generated but smooth terrain.

        create_ground(x,size)
            x       : Seed list, must contain at least two entries.
            size    : Size of the final terrain.
'''

def nextX(x):
    s = 0.99
    i = 1
    a = r.uniform(-i,i)
    v = (x[-1] - x[-2]) + a*s
    x_new = x[-1] + v*s
    x.append(x_new)
    return x

def create_ground(x,size):
    if len(x) < 2 or type(x) != list:
        print("No Seedlist. Default is used. ([1,1])")
        x = [1,1]
    elif size < len(x) or type(size) != int:
        print("False size. Given: {}. Needed: {} \n Size changed to len(x)".format(size, len(x)))
        size = len(x)
    while len(x) < size:
        x = nextX(x)
    z = max([abs(i) for i in x])
    return [abs(i/z) for i in x]
    

if __name__ == '__main__':
    x = [1,1]
    x = create_ground(x, 1000)

    plt.plot(x)
    plt.show()
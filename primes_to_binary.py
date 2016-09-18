import numpy as np
from sys import argv
import matplotlib.pyplot as plt
import cProfile
import re
import pstats
import time
totalTime = time.clock()

# inelegant way to allow people to plot either the differences between
# successive primes or the primes themselves
try:
    # assuming the plot_diffs var is initialized, we'll plot the differences
    # between successive primes, just out of my curiosity to see what it
    # looks like
    script, file_name, how_many, plot_diffs = argv 
except:
    # else, we'll plot the primes themselves
    script, file_name, how_many = argv
    plot_diffs = False

my_nums = np.genfromtxt(file_name)
my_nums = np.ndarray.flatten(my_nums)
my_nums = my_nums[0:int(how_many)]

if not plot_diffs:
    binaries = [np.binary_repr(x,width=24) for x in my_nums]
    x_axis = []
    y_axis = []
    x_appender = x_axis.append
    y_appender = y_axis.append

    # now, get pts with a 1 in them, and make a list of these pts.  For each
    # successive binary number, we need to increment the number we put in the
    # array by a fixed amount, so the plotted pts for each number don't overlap.
    # We then need to append an appropriate value to the end of the x_axis array
    for i in xrange(len(binaries)):
            for bit in xrange(len(binaries[i])):
                    if binaries[i][bit]=='1': # if bit is 1
                            x_appender(bit)
                            y_appender(i)

    plt.hist2d(x_axis,y_axis,bins=[range(26),range(int(how_many)+1)])
    plt.xlim(0,25)
    plt.show()

else:
    # No real reason for plotting the differences; I was just curious to see
    # if there happened to be any pattern in the differences between
    # successive prime numbers
    diffs = [my_nums[i+1] - my_nums[i] for i in xrange(len(my_nums)-1)]
    diffs_x_axis = []
    diffs_y_axis = []

    binary_diffs = [np.binary_repr(x,width=24) for x in diffs]

    for i in xrange(len(binary_diffs)):
        for bit in xrange(len(binary_diffs[i])):
            if binary_diffs[i][bit]=='1':
                diffs_x_axis.append(bit)
                diffs_y_axis.append(i)

    plt.hist2d(diffs_x_axis,diffs_y_axis,bins=[range(26),range(int(how_many)+1)])
    plt.xlim(17 ,25)
    plt.show()

print(time.clock() - totalTime)


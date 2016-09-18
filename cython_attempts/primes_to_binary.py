import numpy as np
from sys import argv
import matplotlib.pyplot as plt
import cProfile
import re
import pstats
import time
totalTime = time.clock()

script, file_name, how_many, plot_diffs = argv
# cProfile.run('everything(file_name,how_many)')
# @profile
# def everything(file_name,how_many):
# my_nums = np.genfromtxt(file_name,dtype=np.int32)
my_nums = np.genfromtxt(file_name)#[:how_many]
# print(my_nums)
my_nums = np.ndarray.flatten(my_nums)
my_nums = my_nums[0:int(how_many)]
# print(my_nums)
if plot_diffs != 'plot_diffs':
    binaries = [np.binary_repr(x,width=24) for x in my_nums]
    # for i in my_nums[:100]:
    # 	print(i)
    # binaries = ['{0:024b}'.format(int(x)) for x in my_nums]

    # print(binaries)
    # x_axis=np.arange(19,-1,-1) # makes array from 19 to 0, one for each bit
    x_axis = []
    y_axis = []
    x_appender = x_axis.append
    y_appender = y_axis.append

    # now, get points with a 1, and make a list of each point that does have a
    # 1.  For each successive binary number, we'll need to increment the number
    # we're putting in the array by a fixed amount, so the plotted points for
    # each number don't overlap.  We'll then need to stick an appropriate value
    # to the end of the x_axis array
    for i in xrange(len(binaries)):
            # print(binaries[i])
            for bit in xrange(len(binaries[i])):
                    # print(binaries[i][bit])
                    if binaries[i][bit]=='1': # if bit is 1
                            x_appender(bit)
                            y_appender(i)

    # print(x_axis)
    # print(y_axis)

    # use matplotlib to plot whether or not a binary number has a 1 in each bit
    # print(plt.hist2d(x_axis,y_axis,bins=[24,int(how_many)]))#,range=[]))
    # print(plt.hist2d(x_axis,y_axis,bins=[range(26),range(int(how_many)+1)]))

    plt.hist2d(x_axis,y_axis,bins=[range(26),range(int(how_many)+1)])
    plt.xlim(0,25)
    plt.show()

    # plt.plot(diffs[-200:],marker='+')
    # plt.xlim(0,len(diffs))
    # plt.ylim(0,max(diffs))
    # plt.show()

elif plot_diffs == 'plot_diffs':
    diffs = [my_nums[i+1] - my_nums[i] for i in xrange(len(my_nums)-1)]
    # print(diffs)
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

else:
    print("Error, bad input (type either 'plot_diffs' or 'no_plot_diffs')")
print(time.clock() - totalTime)

# everything(file_name,how_many)


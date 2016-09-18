import numpy as np
from sys import argv
import matplotlib.pyplot as plt
import cProfile
import re
import pstats
from multiprocessing import *
import time
from itertools import chain
totalTime = time.clock()

script, file_name, how_many = argv
my_nums = np.genfromtxt(file_name)#[:how_many]
my_nums = np.ndarray.flatten(my_nums)
my_nums = my_nums[0:int(how_many)]

binaries = [np.binary_repr(x,width=24) for x in my_nums]

x_axis = []
y_axis = []
x_appender = x_axis.append
y_appender = y_axis.append

# now, get the points with a 1, and make a list of each point that does have a
# one.  For each successive binary number, we'll need to increment the number
# we're putting in the array by a fixed amount, so that the plotted points for
# each number don't overlap.  We'll then also need to stick an appropriate value
# to the end of the x_axis array
def list_maker(binary_number):
	x_row = []
	# y_row = []
	for bit in xrange(len(binary_number)):
		if binary_number[bit]=='1': # if bit is 1
			x_row.append(bit)
			# y_row.append()
	# return x_axis, y_axis
	return x_row
# print(x_axis)
# print(y_axis)

if __name__ == '__main__':
	# results = Pool(processes=cpu_count()).map(list_maker,binaries)
	results = Pool(processes=2).map(list_maker,binaries)
	# print(results)

# for x in xrange(len(results)):

for i in xrange(len(results)):
    for number in xrange(len(results[i])):
        # x_appender(results[i][number])
        #         x_axis.append(number)
        y_appender(i)
        # print(results[i][number])
        # print(results[i])

# x_axis = [item for sublist in results for item in sublist]
x_axis = list(chain.from_iterable(results))
# x_axis = np.array(results)
# print(x_axis)
# print(len(x_axis))
# print(type(x_axis))
# # x_axis = np.reshape(x_axis)#len(y_axis))
# x_axis = x_axis.flatten()
#
# print(x_axis)
# print(len(x_axis))
# print(y_axis)
# use matplotlib to plot whether or not a binary number has a 1 in each bit
# print(plt.hist2d(x_axis,y_axis,bins=[24,int(how_many)]))#,range=[]))
# print(plt.hist2d(x_axis,y_axis,bins=[range(26),range(int(how_many)+1)]))
# print(plt.hist2d(results[0],results[1],bins=[range(26),range(int(how_many)+1)]))
print(plt.hist2d(x_axis,y_axis,bins=[range(26),range(int(how_many)+1)]))

plt.xlim(0,25)
plt.show()
print(time.clock() - totalTime)

# everything(file_name,how_many)


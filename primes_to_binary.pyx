import numpy as np
from sys import argv
import matplotlib.pyplot as plt
import cProfile
import re
import pstats
import time
totalTime = time.clock()

script, file_name, how_many = argv
# cProfile.run('everything(file_name,how_many)')
# @profile
# def everything(file_name,how_many):
# my_nums = np.genfromtxt(file_name,dtype=np.int32)
my_nums = np.genfromtxt(file_name)#[:how_many]
# print(my_nums)
my_nums = np.ndarray.flatten(my_nums)
my_nums = my_nums[0:int(how_many)]
# print(my_nums)

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

# now, get the points with a 1, and make a list of each point that does have a
# one.  For each successive binary number, we'll need to increment the number
# we're putting in the array by a fixed amount, so that the plotted points for
# each number don't overlap.  We'll then also need to stick an appropriate value
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
print(plt.hist2d(x_axis,y_axis,bins=[range(26),range(int(how_many)+1)]))
plt.xlim(0,25)
plt.show()
print(time.clock() - totalTime)

# everything(file_name,how_many)


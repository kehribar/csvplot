#!/usr/bin/env python 
#------------------------------------------------------------------------------
# Basic CSV plotting script
# Each column is plotted at a seperate figure.
#------------------------------------------------------------------------------     
# THE COFFEEWARE LICENSE (Revision 1):
# <ihsan@kehribar.me> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a coffee in return.    
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy
import sys

# TODO: Add proper argument check here
if(len(sys.argv) < 2):    
    print "What is the file name?"
    sys.exit()

print "Reading the text file ..."
readout = numpy.loadtxt(open(sys.argv[1],"rb"),delimiter=",")

[length, fig_cnt] = readout.shape

for x in xrange(0,fig_cnt):
    plt.figure()
    plt.plot(readout[:,x])    
    plt.draw()    
 
print "Drawing ..." 
plt.show()

print "Done!"
sys.exit()

#!/usr/bin/env python3

#author: Ali Teimouri
#author ID: ateimouri1
#Date Created 2024/05/17


import sys

#number = len(sys.argv)

#if we dont have argument, used 3
if len(sys.argv) !=2:
    timer = 3
else:
    #get the timer number by user
    timer = int(sys.argv[1])
#created a countdown with while loop
while timer !=0:
    print(timer)
    timer = timer -1
print ('blast off!')
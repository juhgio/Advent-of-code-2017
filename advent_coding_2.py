# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#author: juho-petteri lesonen
#date: 05.12.2017
#Problem describtion from Advent of code 2017: https://adventofcode.com/2017/day/2

import time
import sys

def check(value):

	num_i = list(map(int, value))
	minimum = min(num_i)
	maximum = max(num_i)
	value_0 = maximum - minimum
	return value_0
	
if __name__ == "__main__":
	print( "Program started." )
	
	start = time.time()
	
	checksum = 0
	arr = sys.argv
	del arr[0]
	
	for i  in arr:
		checksum += check(i)
		
	end = time.time()
	times = end-start
	
		
	print("Result = %s and time elapsed = %s seconds" % (checksum,times))
	print( "Program ended." )

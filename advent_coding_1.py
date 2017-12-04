# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#author: juho-petteri lesonen
#date: 04.12.2017
#Problem description from Advent of code 2017: https://adventofcode.com/2017/day/1

import time
import sys

def testing(value):

	checksum = 0
	num_i = list(map(int, value))
	num_i.append(num_i[0])
	length = len(num_i)-1

	for i in range(length):
		
		if num_i[i] == length:
			break
		
		else:
			if num_i[i] == num_i[i+1]:
				checksum += num_i[i]
	
	return checksum

if __name__ == "__main__":
	print( "Program started." )
	if len(argv) != 2:
    		print(USAGE % argv[0])
    		quit()

	a_1 = sys.argv[1]
	start = time.time()
	result = testing(a_1)
	end = time.time()
	times = end-start
	
	print("Result = %s and time elapsed = %s seconds. "  % (result, times))
	print( "Program ended." )

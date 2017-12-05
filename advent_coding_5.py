# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#author: juho-petteri lesonen
#date: 06.12.2017
#Problem description from Advent of code 2017: https://adventofcode.com/2017/day/5

import time
import sys

def maze_run(maze):
	k = 0
	index = 0
	
	while index < len(maze) or index < 0:
		jump = maze[index]
		new_index = index + jump
		maze[index] = maze[index] + 1
		index = new_index
		k += 1
		
	return k
		
if __name__ == "__main__":
	print( "Program started." )
	start = time.time()
	
	args = sys.argv
	del args[0]
	a_1 = list(map(int,args))
	print(args)
	steps = maze_run(a_1)

	end = time.time()
	times = end - start
	
	print("Steps to make it out of the maze = %s and time elapsed = %s seconds." % (steps, times))

	print( "Program ended." )

# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#author: juho-petteri lesonen
#date: 05.12.2017
#Problem description from Advent of code 2017: https://adventofcode.com/2017/day/3

import time
import sys
import numpy as np

def initial_matrix(value):
	i = 1
	a = 1
	while a < value:
		i = i + 1
		a = i ** 2
	shape = i
	matrice_init = np.arange(1,a+1).reshape(shape,shape)
	return matrice_init

def spiral_open(A):
	A = np.array(A)
	out = []
	while(A.size):
		out.append(A[0][::-1])
		A = A[1:][::-1].T
	return np.concatenate(out)
	
def spiral_indices(nrow, ncol):
	return spiral_open(np.arange(nrow*ncol).reshape(nrow,ncol))[::-1]
		
def matrice_to_spiral(A):
	A = np.array(A)
	B = np.empty_like(A)
	B.flat[spiral_indices(*A.shape)] = A.flat
	return B
	
def distance(start, end):
	x1,y1 = start
	x2,y2 = end
	return abs(x2-x1) + abs(y2-y1)

if __name__ == "__main__":
	print( "Program started." )
	start = time.time()
	
	position  = int(sys.argv[1])
	matrice_initial = initial_matrix(position)
	spiral_matrice = matrice_to_spiral(matrice_initial)
	x0,y0 = np.where(spiral_matrice == 1)
	x1,y1 = np.where(spiral_matrice == position)
	
	dist = int(distance([x1,y1],[x0,y0]))
	
	end = time.time()
	times = end - start
	
	print("Distance  = %s and time elapsed = %s seconds" % (dist,times))
	print( "Program ended." )

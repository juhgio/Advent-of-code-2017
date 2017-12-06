# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#author: juho-petteri lesonen
#date: 05.12.2017
#Problem description from Advent of code 2017: https://adventofcode.com/2017/day/4

import time
import sys

def split_string(phrase):
	unique_words = len(set(phrase))
	number_words = len(phrase)
	if unique_words == number_words:
		return 1
	else:
		return 0


if __name__ == "__main__":
	print( "Program started." )
	start = time.time()

	result = sys.argv
	del result[0]
	a_1 = result
	
	value = split_string(a_1)

	end = time.time()
	times = end - start
	
	if value == 1:
		print("The phrase is valid. Time elapsed = %s seconds." % times)
	else:
		print("The phrase is not valid. Time elapsed = %s seconds." % times)
	print( "Program ended." )

"""
Program to generate English Ruler using Recursion

	Funtion draw : Generates the keys = (x,y) , where x is the number of dashes and y is the line number on which the dash is to be drawn
	For example (4,1) would imply four dashes on line number 1

	This function returns all such keys that aids in drawing the English Ruler

	Parameters to be given to the function during the initial call:
	Param 1 : An empty list to which the keys will be appended
	Param 2 : k-1 , 
	Param 3 : 2**(k-2) + 1 , where k is the maximum major_tick_length

Author : Harish Balakrishnan

"""


def draw(keys,major_tick_length,start_line):
	"""A recursive funtion that draws the English Ruler"""

	keys.append((major_tick_length,start_line))
	if major_tick_length > 1:
		draw(keys,major_tick_length-1,start_line-(2**(major_tick_length-2)))
		draw(keys,major_tick_length-1,start_line+(2**(major_tick_length-2)))
a= []
draw(a,4,9)
print a

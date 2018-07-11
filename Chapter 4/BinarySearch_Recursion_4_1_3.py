"""
Module : Binary Search using Recursion

Function : binary_search_recursion

Author: Harish Balakrishnan

"""

def binary_search_recursion(n,sorted_array,start,end):
	"""Binary Search function Using Recursion
	
	Function Call :  binary_search_recursion(find_no,sorted_array,start_idx,end_idx)

	"""
	l = int((end+start)/2)
	if n == sorted_array[l]:
		return l
	elif n<sorted_array[l]:
		return binary_search_recursion(n,sorted_array,start,l)
	elif n>sorted_array[l]:
		return binary_search_recursion(n,sorted_array,l,end)
	else:
		return -1


if __name__ == '__main__':
	sorted_array = [x for x in range(100)]
	index = binary_search_recursion(48,sorted_array,0,99)
	print 'Sorted Array = {}\n'.format(sorted_array)
	print 'Index As returned by binary_search_recursion(48,sorted_array,0,99) = {}\n'.format(index)
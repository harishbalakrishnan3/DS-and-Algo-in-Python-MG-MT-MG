"""
This module does sequence sum recursively.

Author: Harish Balakrishnan.
"""

def seq_sum_recursive(seq,start,end):
	"""This function calculates the sum of a sequence recursively.

	Example Function Call : Sum = seq_sum_recursive(seq,0,len(seq)-1).
	"""
	if start == end:
		return seq[start]
	elif (start+1) == end:
		return seq[start]+seq[end]
	else:
		return seq[start]+ seq[end] + seq_sum_recursive(seq,start+1,end-1)


if __name__ == '__main__':
	a = [x for x in range(10)]
	print seq_sum_recursive(a,0,len(a)-1)


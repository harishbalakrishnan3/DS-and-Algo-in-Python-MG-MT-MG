"""
This module contains the solutions to the Exercises of Ch 4

Function List : 
max_element_r_4_1
element_uniqueness_c_4_11

Author: Harish Balakrishnan
"""

def max_element_r_4_1(S,n,maxe=0):
	"""Function Call : duplicates  = max_element_r_4_1(List,len(List))"""
	if n == len(S):
		n-=1
		maxe = S[n]
		return max_element_r_4_1(S,n-1,maxe)
	elif n>0:
		if S[n] > maxe:
			maxe = S[n]
		return max_element_r_4_1(S,n-1,maxe)
	else:
		return maxe

def element_uniqueness_c_4_11(S,duplicates=[],first=1,second=0):
	"""Function Call : duplicates  = element_uniqueness_c_4_11(List)"""
	if second == first-1 and first != len(S)-1:
		if S[first] == S[second]:
			duplicates.append(S[first])
		first +=1
		return element_uniqueness_c_4_11(S,duplicates,first,0)
	elif second == first-1 and first == len(S)-1:
		if S[first] == S[second]:
			duplicates.append(S[first])
		return duplicates
	else:
		return element_uniqueness_c_4_11(S,duplicates,first,second+1)

if __name__ == '__main__':
	
	a = [x for x in range(100)]
	print "Sample Array : {}".format(a)
	print "R-4.1 : Maximum Element : {}\n".format(max_element_r_4_1(a,len(a)))

	b = [0,1,2,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
	print "Sample Array : {}".format(b)
	print "C-4.11 : Duplicates : {}\n".format(element_uniqueness_c_4_11(b))	





	



	




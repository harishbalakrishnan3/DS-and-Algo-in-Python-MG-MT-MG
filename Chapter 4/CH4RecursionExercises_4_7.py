"""
This module contains the solutions to the Exercises of Ch 4

Function List : 
MaxElement_r41
NthHarmonicNumber_r46
MaxMin_c49
ElementUniqueness_c411
TowersOfHanoi_c414
PowerSet_c415
StringReverse_c416
VowelsConsonants_c418
OddEven_c419
RearrangementUsingK_c420
SumOfIntegers_c422

Author: Harish Balakrishnan
"""

import random
import copy

def MaxElement_r41(S,n,maxe=0):
	"""Function Call : duplicates  = MaxElement_r41(List,len(List))"""
	if n == len(S):
		n-=1
		maxe = S[n]
		return MaxElement_r41(S,n-1,maxe)
	elif n>0:
		if S[n] > maxe:
			maxe = S[n]
		return MaxElement_r41(S,n-1,maxe)
	else:
		return maxe

def NthHarmonicNumber_r46(n, sum=0):
	"""Function Call : sum = NthHarmonicNumber_r46(n)"""
	if n==1:
		return sum
	else:
		sum += (1/n)
		n -= 1
		return NthHarmonicNumber_r46(n,sum)

def MaxMin_c49(S,n,maxe=0,mine=0):
	"""Function Call : MaxMinList  = MaxMin_c49(ListOfIntegers,len(ListOfIntegers))"""
	if n == len(S):
		n-=1
		maxe = S[n]
		mine = S[n]
		return MaxMin_c49(S,n-1,maxe,mine)
	elif n>0:
		if S[n] > maxe:
			maxe = S[n]
		if S[n] < mine:
			mine = S[n]
		return MaxMin_c49(S,n-1,maxe,mine)
	else:
		return maxe,mine

def ElementUniqueness_c411(S,n,m=0,flag=0):
	"""Function Call : duplicates  = ElementUniqueness_c411(ListOfIntegers,len(ListOfIntegers))"""
	if flag == 1:
		return False
	elif n == 1 and flag == 0:
		return True
	elif m == n-1:
		return ElementUniqueness_c411(S,n-1,0,flag)
	else:
		if S[n-1] == S[m]:
			flag = 1
		m += 1
		return ElementUniqueness_c411(S,n,m,flag)

def TowersOfHanoi_c414(n):
	"""Function Call : NoOfMoves  = TowersOfHanoi_c414(NoOfDisks)"""
	if n ==1:
		return 1
	else:
		return (1+(2*TowersOfHanoi_c414(n-1)))

def PowerSet_c415(S,subsets=[[]]):
	"""Function Call : powerset = PowerSet_c415(list(SampleSet))"""
	if len(S) != 0:
		current = S.pop()
		temp = copy.copy(subsets)
		for element in temp:
			if element == []:
				subsets.append([current])
			else:
				subsets.append(element+[current])
		return PowerSet_c415(S,subsets)
	else:
		return subsets

def StringReverse_c416(string,listOfthisString = []):
	"""Function Call : stringReverse = StringReverse_c416(string)"""
	if not string:
		return ''.join(listOfthisString)
	else:
		temp = list(string)
		if len(temp) != 0:
			listOfthisString.append(temp.pop())
			return StringReverse_c416(''.join(temp),listOfthisString)
		else:
			return ''.join(listOfthisString)

def VowelsConsonants_c418(string,vowels = 0, consonants = 0):
	"""Function Call : Boolvalue = VowelsConsonants_c418(string)"""
	temp = list(string)
	if len(temp) != 0:
		char = temp.pop()
		if char in 'aeiou':
			vowels += 1
		else:
			consonants += 1
		return VowelsConsonants_c418(''.join(temp),vowels,consonants)
	else:
		return vowels>consonants

def OddEven_c419(number,even = [],odd = []):
	"""Function Call : NumberAfterRearrangement = OddEven_c419(number)"""
	listOfthisNumber = list(str(number))
	if len(listOfthisNumber) != 0:
		char = listOfthisNumber.pop(0)
		if char in '02468':
			even.append(char)
		else:
			odd.append(char)
		if len(listOfthisNumber) != 0:
			string = ''.join(listOfthisNumber)
		else:
			string = ''.join(even)
			string += ''.join(odd)
			return int(string)
		return OddEven_c419(int(string),even,odd)

def RearrangementUsingK_c420(number,k,newList = []):
	"""Function Call : RearrangedNumber = RearrangementUsingK(number,k)"""
	listOfthisNumber = list(str(number))
	if len(listOfthisNumber) != 0:
		char = listOfthisNumber.pop()
		if int(char) > k:
			newList.append(char)
		else:
			newList = [char] + newList
		if len(listOfthisNumber) != 0:
			string = ''.join(listOfthisNumber)
			return RearrangementUsingK_c420(int(string),k,newList)
		else:
			return int(''.join(newList))

def SumOfIntegers_c422(number,k,sumPairs = {}):
	"""Function Call : SumPairs = SumOfIntegers_c422(number,k)"""
	listOfthisNumber = list(map(lambda x: int(x),list(str(number))))
	if len(listOfthisNumber) > 1:
		secondNum = listOfthisNumber.pop()
		for x in listOfthisNumber:
			if x+secondNum == k:
				if secondNum not in sumPairs.values():
					sumPairs[secondNum] = x
		return SumOfIntegers_c422(int(''.join(list(map(lambda x: str(x),listOfthisNumber)))),k,sumPairs)
	else:
		return sumPairs

if __name__ == '__main__':
	
	a = [x for x in range(15)]
	random.shuffle(a)
	print("Sample Array : {}".format(a))
	print("R-4.1 : Maximum Element : {}\n".format(MaxElement_r41(a,len(a))))

	c = random.randint(1,5)
	print("N : {}".format(c))
	print("R-4.6 : Harmonic Sum : {}\n".format(NthHarmonicNumber_r46(c)))

	random.shuffle(a)
	print("Sample Array : {}".format(a))
	print("C-4.9 : Maximum Element : {}\nMinimum Element : {}\n".format(MaxMin_c49(a,len(a))[0],MaxMin_c49(a,len(a))[1]))

	b = [4,56,659,458,2,65,12,98,45,659,987]
	random.shuffle(b)
	print("Sample Array : {}".format(b))
	print("C-4.11 : Element Uniqueness : {}\n".format("Yes" if ElementUniqueness_c411(b,len(b)) else "No"))

	print("C-4.14 : Towers of Hanoi for {} disks : {} moves\n".format(4,TowersOfHanoi_c414(4)))

	d={1,2,3,4}
	print("Sample Set : {}".format(d))
	print("C-4.15 : Its powerset : {}\n".format(PowerSet_c415(list(d))))

	string = "Thena"
	print("Sample String : {}".format(string))
	print("C-4.16 : Its reverse using recursion : {}\n".format(StringReverse_c416(string)))

	print("Sample String : {}".format(string))
	print("C-4.18 : String has more vowels than consonants : {}\n".format(VowelsConsonants_c418(string)))

	number = 1234567890
	print("Sample Number : {}".format(number))
	print("C-4.19 : Number after re-arrangement : {}\n".format(OddEven_c419(number)))

	number = 9618124697
	print("Sample Number : {}".format(number))
	print("Sample k Value : 5")
	print("C-4.20 : Number after re-arrangement : {}\n".format(RearrangementUsingK_c420(number,5)))

	print("Sample Number : {}".format(number))
	print("Sample k Value : 10")
	print("C-4.21 : Pairs that sum to k : {}\n".format(SumOfIntegers_c422(number,10)))






	



	




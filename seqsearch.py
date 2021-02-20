#NAMES: Joseph Sembower
#Date: 2/21/17
# Sequential search: in this version, the for loop goes
# through the items in the list dierectly and uses a separate counter

def sequentialSearch(list, testSearchTerm):
	counter = 0 
	for item in list:
		if item == testSearchTerm:
			return counter
		counter = counter +1
	return -1 ##item not found
	
# Sequential search: in this version, the for loop goes
# through the positions of the items in the list
def sequentialSearch2(list, testSearchTerm):
	for checkPos in range(len(list)):
		if list[checkPos] == testSearchTerm:
			return checkPos
	return -1 #indicates searchItem not found

def binarySearch(list, testSearchTerm):
	min =0 
	max = len(list)-1
	
	while min<=max:
		guess = round((min+max)/2)
		if list[guess] == testSearchTerm:
			return guess
		elif list[guess] >testSearchTerm:
			max = guess-1
		elif list[guess]<testSearchTerm:
			min = guess +1
	return guess 
	if max<min:
		return -1   

#main script ################################################################
list = ["ant", "cat", "dog", "elephant", "frog", "goat", "horse", "iguana",
"jackal"]
testSearchTerm = "dog" #change the testSearchTerm for different tests

#test first sequential search algorithm
result = sequentialSearch(list, testSearchTerm)
print ("First sequential search finds ", testSearchTerm, " in position: ", end =
" ")
print(result)

#test second sequential search algorithm
result = sequentialSearch2(list, testSearchTerm)
print ("Second sequential search finds ", testSearchTerm, " in position: ", end
= " ")
print(result)
#test binary search algorithm

result = binarySearch(list,testSearchTerm)
print ("Binary search finds ", testSearchTerm, " in position: ", end = " ")
print(result)
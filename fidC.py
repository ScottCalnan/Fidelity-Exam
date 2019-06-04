# Scott Calnan
# 6/3/19
# Part C
# This console program takes in a string S that is all English alphabet letters and whose length is divisible by three, a string C
# that is all English alphabet letters, and an integer N from the user.  The letters in C are then shifted by N.  Instances of 
# of C in the first third of S are then swapped by instances of C_shift in the remaing two thirds of S. The chacaters of 
# C_shift do not have ot be preceding eachother in this instance.  Unit code of all the functions follows the solution code.

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = ['0','1','2','3','4','5','6','7','8','9']

# takes in a string or array and returns the length of that string or array
def length(string):
	count = 0
	for i in string:
		count += 1
	return(count)

# takes in an array as input and returns it as a string
def make_string(array):
	output = ""
	for i in array:
		output += i
	return output

# takes in a string and returns an array of that string
def make_array(string):
	output = ['']* length(string)
	for i in range(length(string)):
		output[i] = string[i]
	return output

# takes in a string C and integer N then returns a shifted C by N letters
# the function loops from z to a and vice versa
def shift(C,N):
	C = make_array(C)
	for i in range(length(C)):
		for j in range(length(alph)):
			if C[i] == alph[j]:
				C[i] = alph[(j+N)%26]
				break
	return(make_string(C))

# takes in two strings and an integer (index) then determines if string one exists in string two, if not equal retruns -1 otherwise it returns the index
def strings_equal(sub_string, string, start):
	for i in range(length(sub_string)):
		if length(string) > (i+start):
			if sub_string[i] != string[i+start]:
				return -1
				break
	return start

# takes in two strings and returns all indices of sub_string in string
def find_sub_string(string, sub_string):
	indices = []
	first = sub_string[0]
	for i in range(length(string)):
		if string[i] == first:
			index = (strings_equal(sub_string, string, i))
			if index != -1:
				indices += [index]
	return indices

# takes in two strings and returns indices of the dsipersed sub-string in an array
def find_dispersed_sub_string(string, sub_string):
	indices = []
	position = 0
	for j in range(length(string)):
		if position < length(sub_string):
			if string[j] == sub_string[position]:
				indices += [j]
				position += 1
	if length(indices) < length(sub_string):
		return -1
	else:
		return indices

# takes in a string, two substrings, and the indeces in which the sub_strings exist in the string and swaps them 
def swap_strings(full_str,str1,str2,i1,i2):
	str1 = make_array(str1)
	str2 = make_array(str2)
	full_str = make_array(full_str)
	for i in range(length(str2)):
		full_str[i1+i] = str2[i]
		full_str[i2[i]] = str1[i] # this is changed for part C
	return make_string(full_str)

# takes in two strings, C and S, and an integer then returns a modified string with swapped instances of C in the first third of S with instances of C_shift in th eremaining two thirds of S
def switch_instance(S,C,N):
	C_shift = shift(C,N) # create c_shift
	first_third_S = S[0:int(length(S)/3)] # string of the first third of S
	rest_of_S = S[int(length(S)/3):] # the remaining two thirds of S
	# find number of instances to switch
	iterate = length(find_sub_string(first_third_S, C)) 
	for i in range(iterate):
		if (find_sub_string(first_third_S, C)[i] + length(C) < length(first_third_S)): # avoid going past the one third mark when searching for C
			if find_sub_string(first_third_S, C) != -1: # go through first index of C
				i1 = find_sub_string(first_third_S, C)[i] # get index of C
				if find_dispersed_sub_string(rest_of_S, C_shift) != -1:
					i2 = find_dispersed_sub_string(rest_of_S, C_shift) # find dispersed indices
					for i in range(length(i2)):
						rest_of_S = make_array(rest_of_S)
						rest_of_S[int(i2[i])] = ',' #avoids duplicating switching of C_shift
						rest_of_S = make_string(rest_of_S)
						index = i2[i]+length(first_third_S) # transform indices to S string
						i2[i] = index # form swapping index
					S = swap_strings(S, C, C_shift, i1, i2)
	return S

# takes in a string and array then returns a boolean value depending on if there are characters in the string not in the array
def match(input,check):
	for i in range(length(input)):
		if (input[i] in check) == False:
			return False
	return True

# take in user input for S
input_S = input('Please enter a string, S, whose length is divisible by three: ')
state = True
# check if S is all English alphabet letters and divisible by 3
while state:
	if length(input_S)%3 != 0:
		input_S = input('Input error: Length of S is not divisible by 3, please try again: ')
		state = True
	elif match(input_S, alph) == False:
		input_S = input('Input error: S needs all English alphabet letters, please try a new string: ')
		state = True
	else:
		state = False

# take in user input for C		
input_C = input('Please enter a string, C, to be switched: ')
state = True
# check if C is all English alphabet letters
while state:
	if match(input_C, alph) == False:
		input_C = input('Input error: C needs all English alphabet letters, please try a new string: ')
		state = True
	else:
		state = False

# take in user input for N
input_N = input('Please enter an integer, N, to shift C: ')
state = True
# check if N is an integer
while state:
	if match(input_N, num) == False:
		input_N = input('Input error: N needs to be an integer, please try again: ')
		state = True
	else:
		state = False
input_N = int(input_N)

# pring the final modified string, S
print('Your new string: ' + switch_instance(input_S,input_C,input_N))

### UNIT TESTS ###
print('UNIT TESTS:')

# 1- Test length(string) function:
# Input: (string) ==> "Scott"
# Output: (length of string) ==> 5
if length("scott") == 5:
	print("test 1 passed")
else:
	print("test 1 failed")

# 2- Test make_string(array) function:
# Input: (array) ==> ['0','1','2','3','4','5','6','7','8','9']
# Output: (string) ==> '0123456789'
if make_string(['s','c','o','t','t']) == 'scott':
	print("test 2 passed")
else:
	print("test 2 failed")

# 3- Test make_array(string) function:
# Input: (string) ==> 'hello'
# Output: (array) ==> ['h','e','l','l','o']
if make_array('hello') == ['h','e','l','l','o']:
	print("test 3 passed")
else:
	print("test 3 failed")

# 4- Test shift(C,N) function:
# Input: (C,N) ==> ('shifting',3)
# Output: (string) ==> 'crspdsxq'
if shift('shifting',10) == 'crspdsxq':
	print("test 4 passed")
else:
	print("test 4 failed")

# 5- Test strings_equal(sub_string, string, start) function:
# Input: (sub_string, string, start) ==> ('zing','amazing',3)
# Output: (int) ==> 3
if strings_equal('zing','amazing',3) == 3:
	print("test 5 passed")
else:
	print("test 5 failed")

# 6- Test find_sub_string(string, sub_string) function:
# Input: (string, sub_string) ==> ('abcxabcxxbcdxxbcd','abc')
# Output: (array) ==> [0,4]
if find_sub_string('abcxabcxxbcdxxbcd','abc') == [0,4]:
	print("test 6 passed")
else:
	print("test 6 failed")	

# 7- Test find_dispersed_sub_string(string, sub_string) function:
# Input: (string, sub_string) ==> ('abcxabcxxbxxcxdxxbcd','bcd')
# Output: (array) ==> [0,4]
if find_dispersed_sub_string('bxxcxdxxbcd','bcd') == [0,3,5]:
	print("test 7 passed")
else:
	print("test 7 failed")	

# 8- Test swap_strings(full_str,str1,str2,i1,i2) function:
# Input: (full_str,str1,str2,i1,i2) ==> ('abcxxxbxcxd','abc','bcd',0,[6,8,10])
# Output: (string) ==> 'bcdxxxaxbxc'
if swap_strings('abcxxxbxcxd','abc','bcd',0,[6,8,10]) == 'bcdxxxaxbxc':
	print("test 8 passed")
else:
	print("test 8 failed")

# 9- Test switch_instances(S,C,N) function:
# Input: (S,C,N) ==> ('abcxabcxabcxxxxxxxxxxxxxxxxxxxxbcdxxxbxxcxxxdxxbxxcxdxbcd','abc',1)
# Output: (swapped occurences of C in first third of S with occurences of C_shift in remaining two thirds of S) ==> "bcdxbcdxbcdxxxxxxxxxxxxxxxxxxxxabcxxxaxxbxxxcxxaxxbxcxbcd"
if switch_instance('abcxabcxabcxxxxxxxxxxxxxxxxxxxxbcdxxxbxxcxxxdxxbxxcxdxbcd','abc',1) == "bcdxbcdxbcdxxxxxxxxxxxxxxxxxxxxabcxxxaxxbxxxcxxaxxbxcxbcd":
	print("test 9 passed")
else:
	print("test 9 failed")

# 10- Test match(input,check) function:
# Input: (input,check) ==> ('scott', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
# Output: (boolean) ==> True
if match('scott', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == True:
	print("test 10 passed")
else:
	print("test 10 failed")




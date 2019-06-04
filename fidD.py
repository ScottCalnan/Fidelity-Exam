# Scott Calnan
# 6/3/19
# Part D
# This console program takes in a string S that is all English alphabet letters and whose length is divisible by three, a string C
# that is all English alphabet letters, and an integer N from the user.  The letters in C are then shifted by N.  Instances of 
# of C in the first third of S are then swapped by instances of C_shift in the remaing two thirds of S.  Instances of C_shift in the remainder of 
# S can be dispersed through the string and do not need to be consecutive.  This is done by finding the indexes of 
# C and C_shift using a recursive function.  Unit code of all the functions follows the solution code.

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

# takes in a string, a substring, a starting value for the recursive counter (i), an initial value for the indices array, an initial value for the position integer, and an initial value for the temp array
# it returns an array of all dispersed characters of sub_string in string using recursion
def recursive_find_dispersed_sub_string(string, sub_string, i, indices, position, temp):
	if i == length(string): # split the recusion once we have checked all positions in the string
		return indices
	else:
		if string[i] == sub_string[position]:
			temp += [i] # store temporary indices until all characters in sub_string are found
			position +=1 # move to next character in sub_string after match
			if length(temp) !=0 and length(temp)%length(sub_string) == 0: # store the temp values into the actual indices variable once all characters in sub_string have been found in string
				indices += temp
				position = 0
				i = temp[-(length(sub_string))]+1 # start recursion process at index following previous occurance of the first character of sub_string in string
				temp = []
		i += 1
		return recursive_find_dispersed_sub_string(string,sub_string,i,indices,position,temp)

# takes in a string, an integer for the number of swaps to perform, and the indices in which the sub_strings exist in the string and swaps the characters
def swap_strings(full_str,iterate,i1,i2):
	full_str = make_array(full_str)
	for i in range(iterate):
		full_str[i1[i]], full_str[i2[i]]= full_str[i2[i]], full_str[i1[i]] # swap the two characters at their respective indices
	return make_string(full_str)

# takes in two strings, C and S, and an integer then returns a modified string with swapped instances of C in the first third of S with instances of C_shift in th eremaining two thirds of S
def switch_instance(S,C,N):
	C_shift = shift(C,N) # create c_shift
	first_third_S = S[0:int(length(S)/3)] # string of the first third of S
	rest_of_S = S[int(length(S)/3):] # the remaining two thirds of S
	i1 = recursive_find_dispersed_sub_string(first_third_S,C,0,[],0,[]) # find indices of C in first third of S
	i2 = recursive_find_dispersed_sub_string(rest_of_S,C_shift,0,[],0,[]) # find indices of C_shift in remaining two thirds of S
	# find number of swaps to make of C and C_shift
	for i in range(length(i2)):
		i2[i] += length(first_third_S)
	if length(i1) < length(i2):
		iterate = length(i1) # less instances of C
	else:
		iterate = length(i2) # less instances of C_shift
	S = swap_strings(S, iterate, i1, i2) # swap C and C_shift
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

# 5- Test recursive_find_dispersed_sub_string(string, sub_string, i, indices, position, temp) function:
# Input: (string, sub_string, i, indices, position, temp) ==> ('abcxabcxxbcdxxbcd','abc',0,[])
# Output: (array) ==> [0,1,2,4,6,8]
if recursive_find_dispersed_sub_string('abcxaxbxc','abc',0,[],0,[]) == [0,1,2,4,6,8]:
	print("test 5 passed")
else:
	print("test 5 failed")	

# 6- Test swap_strings(full_str,iterate,i1,i2) function:
# Input: (full_str,iterate,i1,i2) ==> ('abcxbcd',3,[0,1,2],[4,5,6])
# Output: (string) ==> 'bcdxabc'
if swap_strings('abcxbcd',3,[0,1,2],[4,5,6]) == 'bcdxabc':
	print("test 6 passed")
else:
	print("test 6 failed")

# 7- Test switch_instances(S,C,N) function:
# Input: (S,C,N) ==> ('abcxxabcxxxxxxxxxxxxxxbcdxxbcd','abc',1)
# Output: (swapped occurences of C in first third of S with occurences of C_shift in remaining two thirds of S) ==> "bcdxxbcdxxxxxxxxxxxxxxabcxxabc"
if switch_instance('abcxxabcxxxxxxxxxxxxxxbcdxxbcd','abc',1) == "bcdxxbcdxxxxxxxxxxxxxxabcxxabc":
	print("test 7 passed")
else:
	print("test 7 failed")

# 8- Test match(input,check) function:
# Input: (input,check) ==> ('scott', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
# Output: (boolean) ==> True
if match('scott', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == True:
	print("test 8 passed")
else:
	print("test 8 failed")


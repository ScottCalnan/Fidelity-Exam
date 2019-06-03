# Scott Calnan
# 6/3/19
# Part B

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
		# print("it is: " + str(i + start))
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
			# print("index is: "+str(i))
			index = (strings_equal(sub_string, string, i))
			if index != -1:
				indices += [index]
	return indices

# takes in a string, two substrings, and the indeces in which the sub_strings exist in the string and swaps them 
def swap_strings(full_str,str1,str2,i1,i2):
	str1 = make_array(str1)
	str2 = make_array(str2)
	full_str = make_array(full_str)
	for i in range(length(str2)):
		full_str[i1+i] = str2[i]
		full_str[i2+i] = str1[i]
	return make_string(full_str)


def recursive_switch(S, C, N, i):
	#Initialize varaibles
	i1 = 0
	i2 = 0
	C_shift = shift(C,N)
	first_third_S = S[0:int(length(S)/3)]
	rest_of_S = S[int(length(S)/3):]
	split = length(S)/3
	# base case is when we reach the end of the first third of S
	if i == length(find_sub_string(first_third_S, C)): # return S once we have reached the split
		return swap_strings(S, C, C_shift, i1, i2) 
	else:
		i += 1
		if (find_sub_string(first_third_S, C)[i] + length(C) < length(first_third_S)):
			if find_sub_string(first_third_S, C) != 1:
				i1 = find_sub_string(first_third_S, C)[i] # use current index to generate swap if the strings are equal
				if find_sub_string(rest_of_S, C_shift) != -1:
					i2 = (find_sub_string(rest_of_S, C_shift)[i] + length(first_third_S)) # if strings are equal grab index to feed into base case
		return recursive_switch(S, C, N, i) # iterate index by index and call the recursive function to see if C and C_shift occur


print(recursive_switch('abcxxabcxxxxxxxxxxxxxxxbcdxxbcd','abc',1, 0))

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

### UNIT TESTS ###

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

# 7- Test swap_strings(full_str,str1,str2,i1,i2) function:
# Input: (full_str,str1,str2,i1,i2) ==> ('abcxbcd','abc','bcd',0,4])
# Output: (string) ==> 'bcdxabc'
if swap_strings('abcxbcd','abc','bcd',0,4) == 'bcdxabc':
	print("test 7 passed")
else:
	print("test 7 failed")


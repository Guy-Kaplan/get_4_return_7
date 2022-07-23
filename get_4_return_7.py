
# Python
# Made by Guy Kaplan - 22.7.22
# Task: Write all funcs that return 7 when the given num is 4.
# Otherwise, return 0 or any other int

# funcs

def get_4_return_7_if(num: int) -> int:
	if num == 4:
		return 7
	return 0

def get_4_return_7_plus(num: int) -> int:
	# NO if is allowed
	return num+3

def get_4_return_7_replace(num: int) -> int:
	# NO if is allowed & any math operator (+,-,*,/,//)
	# 4 (100 in binary) will become 7 (111 in binary)
	num_in_binary_str = str("{0:b}".format(num))  # decimal -> binary
	new_num = num_in_binary_str.replace('0', '1')  # turn all bits on (to 1)
	return int(new_num, 2)  # binary -> decimal

def get_4_return_7_or(num: int) -> int:
	# NO if is allowed & any math operator (+,-,*,/,//)
	# 4 (100 in binary) will become 7 (111 in binary)
	num_in_binary = int("{0:b}".format(num))  # decimal -> binary
	new_num_str = str(num_in_binary | 111)  # turn bits on (to 1)
	return int(new_num_str, 2)  # binary -> decimal
	
# main

num = 4
print(get_4_return_7_if(num))
print(get_4_return_7_plus(num))
print(get_4_return_7_replace(num))
print(get_4_return_7_or(num))





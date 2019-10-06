# PA1
## Description
In PA1, we are required to implement two algorithms to evaluate the similarities of two DNA sequences. To finish the work, I designed two functions to implement the two algorithms. The first one is called sim1. It implemented the ```number of matches```. In sim1, I used two layers of for loop to conduct the method. The outer layer gives how many rounds of shifts. The inner layer gives the range of items which are in sequences abd need to be compared. If the compared items from different sequences are the same, the similarity (here, it is ```cnt```) increases. After each rounds, the similarity is appended to ```list_chain```, and this list variable will be returned after the end of for loops. The second one is called sim2. It implemented the ```maximum contiguous chain```. In sim2, I also used two layers of for loop to conduct the method, and the function of two layers are the same as in sim1. And there is also a variable named ```cnt``` to calculate the continuity (also, it is ```cnt```). If the compared elements from different sequences are the same, ```cnt``` increases on the basis of the previous, but if they are different, ```cnt``` will be set to zero. I used a list called ```list_chain_tmp``` to store all the ```cnt``` in a round, and the maximum element of ```list_chain_tmp``` will be append to another list called ```list_chain```. After for loops are ended, the ```list_chain``` will be returned. The code are listed.
## functions
### get_option
Select the algorithm that will be used to evaluate the two sequences.
```Python
def get_option():
	while(True):
		option = input("please select one option: \n \
		1---Number of matches, calculate how many points in two chains are the same.\n \
		2---Maximum contiguous chain.\n \
		")
		flag = 0
		try:
			option = int(option)
		except ValueError:
			print("you give an invalid value: %s, please select input 1 or 2\n", option)
			flag = 0
		else:
			if option == 1:
				print("you selected number of matches.\n")
				flag = 1
			elif option == 2:
				print("you selected maximum contiguous chain.\n")
				flag = 1
			else: 
				flag = 0
				print("you must select from 1 and 2!\n")
				continue
		if flag == 0:
			continue
		return option
```
### max_shift
```Python
def max_shift(str1, str2):
	a = len(str1)
	b = len(str2)
	max_value = max(a, b)
	while(True):
		shifts = input("please give the maximum shift(must be a non-negative integer):")
		flag = 0
		try:
			shifts = int(shifts)
		except ValueError:
			print("you give an invalid value: %s, please give a non-negative integer only!", shifts)
			flag = 0
		else:
			if shifts >= 0 and shifts <= (max_value-1):
				flag = 1
			else:
				flag = 0
				print("Shifts can not be negative and can not be bigger than the length of input strings : %d" %(max_value-1))
				continue
		if flag == 0:
			continue
		return shifts
```
### input_files
Get the name of input files. If the file doesn't exists or is empty, it is invalid.
```Python
def input_files():
	while(True):
		filename = input("peease give the file name:\n")
		filename = "./" + filename
		print(filename)
		flag = 0
		
		if os.path.exists(filename) == True :
			flag = 1
		else:
			print("file doesn't exists: %s!" %filename)
			flag = 0
		if flag == 0:
			continue

		if os.path.getsize(filename) :
			fiag = 1
		else : 
			print("empty file: %s!" %filename)
			flag = 0
		if flag == 0:
			continue

		return filename
```
### get_sequence
Get the sequence of the given input file. If there are invalid characters in the sequences, users need to make decision whether continue the evaluation.
```Python
def get_sequence(filename):
	f = open(filename, "r")
	line = f.readline().upper()
	line = line.strip('\n')
	print(line)
	for char in line:
		if char != 'A' and char != 'G' and char != 'C' and char != 'T':
			res = input("invalid character(s) detected, continue?(y/n)")
			if res == "y":
				return line
			else:
				exit(0)
	return line
```
### compare_len
Compare the length of sequences and return the results. The result is used to calculate how many '-' will be added to the end of the shorter sequence.
```Python
def compare_len(str1, str2):
	a = len(str1)
	b = len(str2)
	if a > b:
		return 1, a-b
	elif a < b:
		return 2, b-a
	else:
		return 3, 0
```
### sim1
```Python
def sim1(str1, str2, shift): 
	a = len(str1)
	b = len(str2)
	list_chain = []
	list_chain_tmp = []
	cnt = 0
	shift_tmp = -1
	similarity = 0
	position = 0

	for cnt1 in range(0, shift+1):
		for cnt2 in range(0, a-cnt1):
			if str1[cnt2] == str2[cnt1+cnt2]:
				cnt = cnt + 1
		list_chain.append(cnt)
		cnt = 0
	return list_chain
```
### sim2
```Python
def sim2(str1, str2, shift):
	a = len(str1)
	b = len(str2)
	list_chain = []
	list_chain_tmp = []
	cnt = 0

	for cnt1 in range(0, shift+1):
		for cnt2 in range(0, a-cnt1):
			if str1[cnt2] == str2[cnt1+cnt2]:
				cnt = cnt+1
			else:
				cnt = 0
			list_chain_tmp.append(cnt)
		cnt = 0
		print(list_chain_tmp)
		list_chain_tmp.sort(reverse=True)
		list_chain.append(list_chain_tmp[0])
		list_chain_tmp.clear()	
	print(list_chain)
	return list_chain
```
### sim_output
This function is used to output the results. ```max_value1``` and ```max_value2``` are used to get the biggest value of ```list_chain1``` and ```list_chain2```, respectively. ```list_max1``` and ```list_max2``` are used to get all the ```shifts``` which match the ```max_value1``` and ```max_value2```, respectively. ```list_max1``` and ```list_max2``` are used to calculate how many '-' will be added to sequences.
```Python
def sim_output(str1, str2, list_chain1, list_chain2):
	str1_tmp=str1
	str2_tmp=str2
	max_value1 = 0
	max_value2 = 0
	shift_tmp1 = 0
	shift_tmp2 = 0
	list_max1 = []
	list_max2 = []
	list_max_tmp = []
	for item in list_chain1:
		if item > max_value1:
			max_value1 = item

	for item in list_chain2:
		if item > max_value2:
			max_value2 = item
	
	for item in list_chain1:
		if item == max_value1:
			list_max1.append(shift_tmp1)
		shift_tmp1 = shift_tmp1+1
	
	for item in list_chain2:
		if item == max_value2:
			list_max2.append(shift_tmp2)
		shift_tmp2 = shift_tmp2+1
	
	print(list_max1)
	print(list_max2)

	if max_value1 > max_value2:
		for item in list_max1:
			str1 = "-"*item + str1_tmp
			str2 = str2_tmp + "-"*item
			print("similarity is %d" %max_value1)
			print("sequence 1 -> %s" %str1)
			print("sequence 2 -> %s" %str2)
			print("\n")

	elif max_value1 < max_value2:
		for item in list_max2:
			str1 = str1_tmp + "-"*item
			str2 = "-"*item + str2_tmp
			print("similarity is %d" %max_value2)
			print("sequence 1 -> %s" %str1)
			print("sequence 2 -> %s" %str2)
			print("\n")

	elif max_value1 == max_value2:
		if list_max1[0] == 0:
			list_max2 = list_max2[1:]
		for item in list_max1:
			str1 = "-"*item + str1_tmp
			str2 = str2_tmp + "-"*item
			print("similarity is %d" %max_value1)
			print("sequence 1 -> %s" %str1)
			print("sequence 2 -> %s" %str2)
			print("\n")

		for item in list_max2:
			str1 = str1_tmp + "-"*item
			str2 = "-"*item + str2_tmp
			print("similarity is %d" %max_value2)
			print("sequence 1 -> %s" %str1)
			print("sequence 2 -> %s" %str2)
			print("\n")
```

### main function
```Python
if __name__ == "__main__":

	list_chain1 = []
	list_chain2 = []

	option = get_option()
	file_name1 = input_files()
	str1 = get_sequence(file_name1)
	file_name2 = input_files()
	str2 = get_sequence(file_name2)
	shifts = max_shift(str1, str2)
	
	comp, result = compare_len(str1, str2)
	if comp == 1 : 	
		str2=str2 + '-'*result
	elif comp == 2 : 
		str1=str1 + '-'*result

	if option == 1:
		list_chain1 = sim1(str1, str2, shifts)
		list_chain2 = sim1(str2, str1, shifts)
	elif option == 2:
		list_chain1 = sim2(str1, str2, shifts)
		list_chain2 = sim2(str2, str1, shifts)
	sim_output(str1, str2, list_chain1, list_chain2)
```
## Discussion
In PA1, the biggset problem I have been faced with is how to use one function to output the results of two algorithms and finally I chose list to finish the task. In this assignment, I get familiar with Python list and other knowledge about Python. That's great!

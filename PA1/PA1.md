# PA1
## Description
### validation
in order to make sure the inputs are valid, I defined a function named validation. Firstly, if the input string is empty, the function will print that `input can not be empty` and exit the program. Secondly, replace `A,G,C,T` with `""`. If the remaining string equals to `""`, the input string is valid. Otherwise, the string is invalid and the program will be exited. The source code is listed below.
```Python
def validation(str1):
	if str1 == "" :
		print("input can not be empty")
		exit(1)
	a = str1
	a = a.replace('A', '')
	a = a.replace('G', '')
	a = a.replace('C', '')
	a = a.replace('T', '')
	if a == "":
		return True
	else :
		print("input not valid")
		exit(1)
```
### compare_len
This function is used to compare the length of two input string. The two strings are called `str1` and `str2`. If str1 is longer than str2, the function will return `1` and the difference of length. If str2 is longer than str1, the function will return `2` and the difference of length. If they have the same length, the function will return `3` and `0`. The source code is listed below.
```Python
def compare_len(str1, str2):
	a = len(str1)
	b = len(str2)
	if a > b :
		return 1, a-b
	elif a < b :
		return 2, b-a
	else :
		return 3, 0
```
### measurement
This function is used to measure the similarity of two input strings. In this function, two for loop are used to compare each element of two strings. The outer for loop indicates how many rounds are needed, and the inner loop indicates in each round how many times are needed two compare each elements. In the inner loop, if the elements are the same, `the variable cnt will plus 1`. After each inner loop, `cnt` will be compared with `similarity`, if `cnt` is bigger, `the old similarity` will be replaced with `cnt` and `the old shift` will be replaced with `shift_tmp`. `After that, cnt will be assigned to 0`. `Shift` is used to measure the shifts of each round.  There is also a list `list_chain_tmp `to record the location of the same elements in each round. If `cnt` is bigger than `similarity`, `list_chain` will be assigned with `list_chain_tmp`. After that, `list_chain_tmp` will be assigned with empty. The source code is listed below.
```Python
def measurement(str1, str2): 
	a = len(str1)
	b = len(str2)
	print(str1, a)
	print(str2, b)
	list_chain = []
	list_chain_tmp = []
	cnt = 0
	shift = 0
	shift_tmp = -1
	similarity = 0
	position = 0
	for cnt1 in range(0, a):
		for cnt2 in range(0, a-cnt1):
			if b-1-cnt2 >= 0 :
				if str1[a-1-cnt1-cnt2] == str2[b-1-cnt2]:
					#print("str1, str2", str1[a-1-cnt1-cnt2], str2[b-1-cnt2])
					cnt = cnt + 1
					list_chain_tmp.append(a-1-cnt1-cnt2)
					#print("str1, str2", a-1-cnt1-cnt2, b-1-cnt2)
					#print("cnt", cnt)
			else : 
				break
		shift_tmp = shift_tmp + 1
		if similarity < cnt:
			similarity = cnt
			shift = shift_tmp
			list_chain = list_chain_tmp
		cnt = 0
		list_chain_tmp = []
		#print("----------similarity, times, shift------------", similarity, cnt1, shift)

	return similarity, shift, list_chain
```
### read_sequence
This function is used to read a string from the assigned file. Try

import sys
import os

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

def compare_len(str1, str2):
	a = len(str1)
	b = len(str2)
	if a > b:
		return 1, a-b
	elif a < b:
		return 2, b-a

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

def read_sequence(file):
	try:
		with open(file, 'r') as f:
			line = f.readline()
			line = line.replace('\n', '')
			return line.upper()
	finally:
		if f:
			f.close()

def write_sequence(file, str1):
	try:
		with open(file, 'a') as f:
			str1 = str1 + '\n'
			line = f.write(str1)
	finally:
		if f:
			f.close()

def write_output(file, str1, str2):
	if os.path.exists("./output.txt") :
		os.system("rm output.txt")
	write_sequence(file, str1)
	write_sequence(file, str2)
	
if __name__ == "__main__":
	similarity_final = 0
	similarity1 = 0
	similarity2 = 0
	shift1 = 0
	shift2 = 0
	list_chain_1 = []
	list_chain_2 = []
	
	str1 = read_sequence("./input_a.txt")
	str2 = read_sequence("./input_b.txt")
	
	validation(str1)
	validation(str2)

	comp, result = compare_len(str1, str2)
	if comp == 1 : 	
		str2=str2 + '-'*result
	else : 
		str1=str1 + '-'*result

	print("str1=",str1)
	print("str2=",str2)
	
	similarity1, shift1, list_chain_1 = measurement(str1, str2)
	similarity2, shift2, list_chain_2 = measurement(str2, str1)
	print("--------------------------output-----------------------")
	if similarity1 > similarity2 :
		similarity_final = similarity1
		start = list_chain_1[-1]
		end = list_chain_1[0]
		str1 = '-'*shift1 + str1
		str2 = str2 + '-'*shift1
		str1 = str1[0:start] + "  " + str1[start:end+1] + "  " + str1[end+1:len(str1)]
		str2 = str2[0:start] + "  " + str2[start:end+1] + "  " + str2[end+1:len(str2)]
	else :
		similarity_final = similarity2
		start = list_chain_2[-1] + shift2
		end = list_chain_2[0] + shift2
		str1 = str1 + '-'* shift2
		str2 = '-'* shift2 + str2
		str1 = str1[0:start] + "  " + str1[start:end+1] + "  " + str1[end+1:len(str1)]
		str2 = str2[0:start] + "  " + str2[start:end+1] + "  " + str2[end+1:len(str2)]
	print("shift1", shift1)
	print("shift2", shift2)
	print(str1)
	print(str2)
	write_output("./output.txt", str1, str2)
	print("the similarity is : ", similarity_final)			

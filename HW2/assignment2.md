# Assignments 2
**note**: All of the functions are in the file "assignment.py", so I firstly use "import assignment2" to import the modules
## 1
### source code
```Python
import numpy
def pythagoreanTheorem(length_a, length_b):
	length_c = numpy.sqrt(numpy.square(length_a) + numpy.square(length_b))
	print(length_c)
```
### results
```Python
>>> assignment2.pythagoreanTheorem(2, 2)
2.8284271247461903
>>> assignment2.pythagoreanTheorem(3,4)
5.0
>>> assignment2.pythagoreanTheorem(6,8)
10.0
```
## 2
### description
In this function, I use the list.append() and for loop to deal with the input. "x%2" is used to decide whether the current element of the list is a odd number. If it is odd, the tripled number will be append in the last of the output list. If the elenemt is odd, the doubled number number will be append in the last of the output list.
### source code
```Python
def list_mangler(list_in):
	print(list_in)
	list_out = list()
	for x in list_in:
		if x%2==0 :
			list_out.append(x*2)
		else :
			list_out.append(x*3)
	print(list_out)
```
### results
```Python
>>> import assignment2 as a2
>>> a2.list_mangler([1,2,3,4])
[3, 4, 9, 8]
>>> a2.list_mangler([2,3,4,5])
[4, 9, 8, 15]
>>> a2.list_mangler([3,4,5,6])
[9, 8, 15, 12]
```
## 3
### description
In this function, I use the list.sort() to sort the elements of the list. After that, the smallest element will be in the last of the list. So, I use "[]" to intercept the list. Finally, I calculate the average of the remaining grades and give the corresponding level.
### source code
```Python
def grade_calc(grades_in, to_drop):
	grades_in.sort(reverse=True)
	grades_in = grades_in[0:-to_drop]
	total = 0
	grade = 0
	for x in grades_in:
		total = total + x
	grade = total/len(grades_in)
	if grade >= 90:
		print("A")
	elif grade >= 80:
		print("B")
	elif grade >= 70:
		print("C")
	elif grade >= 60:
		print("D")
	else :
		print("F")
```
### results
```Python
>>> a2.grade_calc([100, 90, 80, 95], 2)
A
>>> a2.grade_calc([80,80,80,80], 2)
B
>>> a2.grade_calc([70,70,70,70], 2)
C
```
## 4
### description
In this function, I use list.append() and list.clear() to finish the work. Firstly, use for loop and "if" to deal with all of the elements. if the element is odd, tit will be append to the list "odd_number", otherwise it will be append to the list "even_number". Secondly, use list.clear() to clear the input list. Finally, use list.append() to append "even_number" and "odd_number" to the input list.
### source code
```Python
def odd_even_filter(numbers):
	odd_numbers = list()
	even_numbers = list()
	for x in numbers:
		if(x%2==0) :
			even__numbers.append(x)
		else :
			odd_numbers.append(x)
	numbers.clear()
	numbers.append(even_numbers)
	numbers.append(odd_numbers)
	print(numbers)
```
### results
```Pythoni
>>> a2.odd_even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9])
[[2, 4, 6, 8], [1, 3, 5, 7, 9]]
>>> a2.odd_even_filter([3, 9, 43, 7])
[[], [3, 9, 43, 7]]
>>> a2.odd_even_filter([71, 39, 98, 79, 5, 89, 50, 90, 2, 56])
[[98, 50, 90, 2, 56], [71, 39, 79, 5, 89]]
```

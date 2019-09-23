import numpy
def pythagoreanTheorem(length_a, length_b):
	length_c = numpy.sqrt(numpy.square(length_a) + numpy.square(length_b))
	print(length_c)

def list_mangler(list_in):
	list_out = list()
	for x in list_in:
		if x%2==0 :
			list_out.append(x*2)
		else :
			list_out.append(x*3)
	print(list_out)

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


if __name__ == "__main__":
	print("in main")
	list_mangler([1,2,3,4])
	list_mangler([2,3,4,5])
	list_mangler([3,4,5,6])
	grade_calc([100, 90, 80, 95], 2)
	grade_calc([80,80,80,80], 2)
	grade_calc([70,70,70,70], 2)
	odd_even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9])
	odd_even_filter([3, 9, 43, 7])
	odd_even_filter([71, 39, 98, 79, 5, 89, 50, 90, 2, 56])


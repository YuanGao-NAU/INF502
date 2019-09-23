import json as js

def wallets1():
	values = []
	cnt = 0
	while True:
		value = input("How much do you have?\n")
		try:
			value = float(value)
		except ValueError:
			print("you give the invalid value: %s" %value)
		else:
			values.append(value)
			cnt = cnt + 1
		if cnt == 5:
			break
	values.sort(reverse=True)
	print("The fattest wallet has $%f value in it.\n" %values[0])
	print("The skinniest wallet has $%f value in it.\n" %values[-1])
	print("All together, these wallets have $%f value in them.\n" %sum(values))
	print("All together, the total value of these wallets is worth $%f dimes.\n" %(sum(values)*10))


def periodic_table():
	properties = {"symbol", "name", "number", "row", "column"}
	f = open("./Periodic-Table-JSON/new_table.json", 'rb+')
	f_json = js.load(f)
	f.close()
	elements = f_json["elements"]
	while True:
		option = input("please input one option between 0 to 5:\n")
		try:
			option = int(option)
		except ValueError:
			print("you give the invalid option: %s" %option)
			continue
		else:
			if (option>5 or option<1):
				continue
		if option == 1 :		
			option_1(elements)
		elif option == 2 :
			option_2(elements)
		elif option == 3 :
			option_3(elements)
		elif option == 4 :
			option_4(elements)
		elif option == 5:
			return
				


def option_1(elements):
	symbol = input("please input a symbol of the element:")
	symbol = str(symbol)
	flag = 0
	#except
	for element in elements:
		if symbol == element["symbol"]:
			flag = 1
			print("symbol : %s" %element["symbol"])
			print("name : %s" %element["name"])
			print("number : %s" %element["number"])
			print("row : %s" %element["row"])
			print("column : %s" %element["column"])
			break
	if flag == 0 :
		print("no such element: %s" %symbol)

def option_2(elements):
	properties = {"symbol", "name", "number", "row", "column"}
	symbol = input("please input a property of the elements:")
	symbol = str(symbol)
	flag = 0
	for sym in properties:
		if(sym == symbol) :
			flag = 1
	if flag == 0 :
		print("no such property: %s" %symbol)

	for element in elements:
		print("element:%s, %s : %s" %(element["symbol"], symbol, element[symbol]))

def option_3(elements):
	flag = 0
	flag1 = 0
	while (flag==0):
		symbol = str(input("enter the symbol of the element:"))
		name = str(input("enter the name of the element:"))
		number = input("enter the number of the element:")
		row = input("enter the row of the element:")
		column = input("enter the column of the element:")

		try:
			number = int(number) 
		except ValueError:
			print("you give the invalid number of element: %s" %number)
			flag = 0
		else:
			number = str(number) 
			for element in elements:
				if int(element["number"]) == int(number):
					print("The element already exists, symbol: %s,  atomic number: %s" %(element["symbol"], number))
					flag1 = 1
					break
			if flag1 == 1:
				flag = 0
			else :	
				flag = 1
		try:
			row = int(row) 
		except ValueError:
			print("you give the invalid row of element: %s" %row)
			flag = 0
		else:
			if row < 0 :
				print("you give the invalid row of element: %s, row must be positive" %row)
				flag = 0
			row = str(row)
			if flag == 1:
				flag = 1
		try:
			column = int(column) 
		except ValueError:
			print("you give the invalid column of element: %s" %column)
			flag = 0
		else:
			if column < 0 or column > 18:
				print("you give the invalid column of element: %s, column must be positive and less than 18(included)" %column)
				flag = 0
			column = str(column)
			if flag == 1:
				flag = 1
		if flag == 1 :
			dict_0 = {"symbol":symbol, "name":name, "number":number, "row":row, "column":column}
			#s = js.dumps(dict_0)
			elements.append(dict_0)
			s1 = js.dumps(elements)
			js_file_temp = {}
			js_file_temp["elements"] = elements
			json_str = js.dumps(js_file_temp)
			#print(s, type(s))
			print(s1, type(s1))
			f = open("./Periodic-Table-JSON/new_table.json", 'w+')
			f.writelines(json_str)
			f.close()

def option_4(elements):
	flag = 0
	flag1 = 0
	while (flag==0):
		symbol = str(input("please input the symbol of the element:"))
		for element in elements:
			if element["symbol"] == symbol:
				flag = 1
				while (flag1==0):
					name = str(input("enter the name of the element:"))
					number = input("enter the number of the element:")
					row = input("enter the row of the element:")
					column = input("enter the column of the element:")
			
					try:
						number = int(number) 
					except ValueError:
						print("you give the invalid number of element: %s" %number)
						flag1 = 0
					else:
						number = str(number) 
						flag1 = 1
					try:
						row = int(row) 
					except ValueError:
						print("you give the invalid row of element: %s" %row)
						flag1 = 0
					else:
						if row < 0:
							print("you give the invalid row of element: %s, row must be positive" %row)
							flag1 = 0
						row = str(row)
						if flag1 == 1:
							flag1 = 1
					try:
						column = int(column) 
					except ValueError:
						print("you give the invalid column of element: %s" %column)
						flag1 = 0
					else:
						if column < 0 or column > 18:
							print("you give the invalid column of element: %s, column must be positive and less than 18(included)" %column)
							flag1 = 0
						column = str(column)
						if flag1 == 1:
							flag1 = 1
					if flag1 == 1:
						element["name"] = name
						element["number"] = number
						element["row"] = row
						element["column"] = column
						js_file_temp = {}
						js_file_temp["elements"] = elements
						js_file_temp["elements"] = elements
						json_str = js.dumps(js_file_temp)
						f = open("./Periodic-Table-JSON/new_table.json", 'w+')
						f.writelines(json_str)
						f.close()

						

		if flag == 0:
			print("you give the invalid element symbol : %s" %symbol)

		

if __name__ == "__main__":
	#wallets1()
	periodic_table()
		

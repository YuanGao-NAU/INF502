grades = {'John' : 90; 'Paul' : 84, 'ben' : 70, 'Tony' : 35, 'Kate' : 100}
while(True) :
	option = int(input("what youwant to do?\n"))
	if option == 1:
		name = str(input("input one name:\n"))
		print(grades[name])
	elif option==2 :
		name=str(input("give a name:\n"))
		grade=int(input("give a score:\n"))
		grades[name] = grade
	else:
	`
		

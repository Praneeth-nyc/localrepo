a=int(input("Enter a :"))
b=int(input("Enter b :"))
print(f"addition of {a} and {b} is {a+b}")

def multiplication(a,b):
	print(f"product of {a} and {b} is {a+b}")

def division(a,b):
	print(f"division of {a} and {b} is {a/b}")

def subtrction(a,b):
	print(f"difference between {a} and {b} is {a-b}")


print("1.add\n2.subtract\n3.multiply\n4.division\n5.exit\n")
choice=int(input("Enter  choice :"))
while(True):
	if choice==1:
		addition(a,b)
	elif choice==2:
		subtraction(a,b)
	elif choice==3:
		multiplication(a,b)
	elif  choice==4:
		division(a,b)
	elif  choice==5:
		exit
	else:
		print("Invalid Entry")

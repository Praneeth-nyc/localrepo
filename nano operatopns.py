[1mdiff --git a/operations.py b/operations.py[m
[1mindex c73e2bd..3e16a65 100644[m
[1m--- a/operations.py[m
[1m+++ b/operations.py[m
[36m@@ -1,6 +1,28 @@[m
 a=int(input("Enter a :"))[m
 b=int(input("Enter b :"))[m
 print(f"addition of {a} and {b} is {a+b}")[m
[32m+[m[32m<<<<<<< HEAD[m
[32m+[m
[32m+[m[32mdef multiplication(a,b):[m
[32m+[m	[32mprint(f"product of {a} and {b} is {a+b}")[m
[32m+[m
[32m+[m[32mprint("1.add\n2.subtract\n3.multiply\n4.division\n5.exit\n")[m
[32m+[m[32mchoice=int(input("Enter  choice :"))[m
[32m+[m[32mwhile(True):[m
[32m+[m	[32mif choice==1:[m
[32m+[m		[32maddition(a,b)[m
[32m+[m	[32melif choice==2:[m
[32m+[m		[32msubtraction(a,b)[m
[32m+[m	[32melif choice==3:[m
[32m+[m		[32mmultiplication(a,b)[m
[32m+[m	[32melif  choice==4:[m
[32m+[m		[32mdivision(a,b)[m
[32m+[m	[32melif  choice==5:[m
[32m+[m		[32mexit[m
[32m+[m	[32melse:[m
[32m+[m		[32mprint("Invalid Entry")[m
[32m+[m[32m=======[m
  [m
 def division(a,b):[m
 	print(f"division of {a} and {b} is {a/b}")[m
[32m+[m[32m>>>>>>> division[m

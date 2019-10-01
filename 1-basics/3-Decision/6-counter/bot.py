#program to counter 
number1=int(input("please enter first whole number"))
print(str(number1))
number2=int(input("Please enter Second whole number"))
print(str(number2))
number3=int(input("please enter third whole numer"))
print(str(number3))
evencount= 0
oddcount= 0
if number1 % 2==0:
    evencount = evencount + 1
else:
    oddcount= oddcount +1
if number2 % 2==0:
    evencount = evencount + 1
else:
    oddcount= oddcount +1
if number3 % 2==0:
    evencount = evencount + 1
else:
    oddcount= oddcount +1
print(str(evencount) +str(oddcount))
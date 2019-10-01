#code to work out od and even number
num=int(input("Please enter a whole number "))
mod = num % 2 ## this modulo operator works out if the whole number is odd or even
if mod > 0:
    print ("This is an odd number")
else:
    print("This is an even number.")

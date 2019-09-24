name =input("What is your name human?")
age =int(input("How old are you (In years)?"))
hight =float(input("how tall are you (in meters)?"))
Weight =int(input("How much do you weigh(in kilograms)?"))
bmi = Weight/hight*hight
print(name + " you are "  + str(age)+" years old and your BMI is" +str(bmi))
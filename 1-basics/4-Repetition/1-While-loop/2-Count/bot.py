#Useing while loop to remove cables 
count= 0
cables= int( input("How many cables must  i aviod?")) 
while count < cables:
    count+= 1
    print("Avoiding...Done " + str(count) + " Live cables avoided")
    
print("ALL cables avoided ")

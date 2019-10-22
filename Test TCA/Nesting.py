health = 100
count = 5
print("your health is " + str(health) + " Escape in progress")
for count in range(count, 0, -1):
    responce=input("..Oh dearm who is that?")
    if responce =="Smiler's Bot":
        health=health -20
        print("Time to jam out of here")
    elif responce=="Hacker":
        health=health +20
        print("Yay! Better follow this one!")
    else:
        print("phew,Just another emoji!")

print ("Escaped! Health is ", str(health) + "%")

#  def fuctions and useing a for loop to display number of steps crossed
def cross_bridge(steps):
    if steps >5:
        print("The bridge is collapsing!")
    for count in range(steps, 0, -1):
            print("Crossed Steps")
    if steps<=5:
        print("Crossed steps")
    for count in range (steps, 0, -1):
        print ("Crossed Steps")
    else:
        print("We must keep going")    
 
cross_bridge(3)
cross_bridge(6)




def display_ladder(Steps):
    for count in range (0 ,Steps, 1 ):
        print("| |")
        print("***")

def create_ladder():
    steps=int(input("How many steps remain"))
    display_ladder(steps)
    
    
create_ladder()

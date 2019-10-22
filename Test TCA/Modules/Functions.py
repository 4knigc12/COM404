## Fuctions for use in the main.py file
def under(word):
    for posision in range(0, len(word), 1):
        print("" + str(posision) + "*"))

def over(word):
    for posision in range(0, len*(word),1):
        print("" +str(posision) "* ")

def both(word):
    for posision in range(0, len*(word),1):
        print("" +str(posision) "*")

def grid(word):
    for posision in range(0, len*(word),1):
        print("" +str(posision) "*")

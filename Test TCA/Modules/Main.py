from Functions import under
def run():  
    Word=input("Please enter your word")
    option=input("What fuction Would you like")
    if option =="under":
        under()
    elif option=="over":
        over()
    elif option=="both":
        both()
    elif option=="grid":
        grid()

run()
from Functions import under
def run():  
    Word=input("Please enter your word")
    option=input("What fuction Would you like")
    if option =="under":
        run(under)
    elif option=="over":
        Run(over)
    elif option=="both":
        Run(both)
    elif option=="grid":
        run(grid)

run()
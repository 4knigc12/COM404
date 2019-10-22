def is_league_united(hero1,hero2):
    if hero1 =="Superman" and hero2 =="Wonder Woman":
        return True
    else:
        return False
print()
def decide_plan(hero1,hero2):
    responce=is_league_united(hero1,hero2)
    if responce== True:
        print("Time to save the wold!")
    else:
        print("We must united the leageue")
print()
def run():
    hero1=input("Name of first hero ")
    hero2=input("Name of Second Hero ")
    plan=input("Enter the plan ")
    if plan == "league":
        is_league_united(hero1,hero2)
    elif plan == "plan":
        decide_plan(hero1,hero2)
    else:
        print("Invalid command. Please try again ")

run()   
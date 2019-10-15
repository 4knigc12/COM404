def escape_by(plan):
    if plan =="jumping over":
        print("We cannot escape that way! The boulder is too big!")
        return escape_by
    if plan =="running around":
        print("We cannot escape that way! The boulder is moving too fast!")
        return escape_by
    if plan == "going deeper":
        print("That might just work! Let's go deeper")
        return escape_by
    else:
        print("We cannot escape that way! The boulder is in the way")

escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")
print()
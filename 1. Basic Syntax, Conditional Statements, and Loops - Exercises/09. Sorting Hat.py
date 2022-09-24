name = input()
while name != "Welcome!":
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif name == "Voldemort":
        break
    else:
        print(f"{name} goes to Hufflepuff.")
    name = input()
if name == "Welcome!":
    print("Welcome to Hogwarts.")
else:
    print("You must not speak of that name!")
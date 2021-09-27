## <---The Game of Software Engineering---> 
## This game will be a map of decisions you can make throughout your career: 
## FrontEnd, BackEnd, or DevOps
## Write unit tests or do not 
## Learn a framework or reinvent the wheel
## Climb the ranks to becoming a Senior Software Engineer,
## a Tech Lead, a Manager, and watch you're pay increase grow
## along with your responsibilities


from sys import exit

def junior_engineer(path):
    print("You have much to learn young padawan...")
    print(path, "engineering is not for the faint of heart.")
    print("Do you like to code in you're free time?")

    choice = input("> ")

    if choice == "yes":
        mid_engineer()
    elif choice == "no":
        dead("Have fun being poor...just kidding...maybe not.")
    else:
        print("In as fewest words as possible, please.")


def mid_engineer():
    print("So you like to code in your free time eh?")
    print("Do you like to write unit tests?")

    choice = input("> ")

    if choice == "yes":
        print("Have you studied data structures and algorithms?")

        choice = input("> ")

        if choice == "yes":
            senior_engineer()
        else: 
            mid_engineer()

    elif choice == "no":
        mid_engineer()

    else: 
        print("You sure are a talker...")


def senior_engineer():
    print("Holy crap! You're still here??")
    print("Want to help me put out this fire?")

    choice = input("> ")

    if choice == "yes":
        print("I will never forget this...")
        senior_engineer()
    elif choice == "no":
        fired()
    else:
        print("Wat?")


def dead(why):
    print(why)
    exit(0)


def fired():
    exit(0)


def early_career():
    print("Hello World!")
    print("So you want to be a developer huh?")
    print("Do you want to work in the FrontEnd, BackEnd, or DevOps?")

    choice = input("> ")

    if choice == "FrontEnd":
        print("May God have mercy on your soul")
        exit(0)
    elif choice == "BackEnd":
        print("Well what a bright and promising career lies ahead for you")
        junior_engineer(choice)
    elif choice == "DevOps":
        print("May God have mercy on your soul")
        exit(0)
    else:
        print("Hmm... not sure I know that one")
        exit(0)

early_career()
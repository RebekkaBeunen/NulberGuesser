import random


def checkinput(nmr):
    if nmr == 'hard':
        hard()
    elif nmr == 'easy':
        easy()
    elif nmr == 'exit':
        exit()
    while nmr == '' or nmr.isdigit() == False:
        print("Invalid, please make sure to enter a number.")
        nmr = input("Choose number: ")
        if nmr == 'hard':
            hard()
        elif nmr == 'easy':
            easy()
        elif nmr == 'exit':
            exit()
    nmr = int(nmr)
    return nmr

def easy():
    nr = checkinput(input("Choose number: "))

    while nr >= 11 or nr == 0:
        print("Number must be between 1 and 10!")
        nr = checkinput(input("Choose number: "))

    r1 = random.randint(1, 10);
    print(r1)
    if nr == r1:
        #random1 = random.choices("Amazing!", "Good job!", "Genie?", "Hacker?")
        #print(random1)
        print("Good job! +20")
    if nr != r1:
        print("Auwch, -10")
    easy()

def hard():
    nr = checkinput(input("Choose number: "))

    while nr >= 101 or nr == 0:
        print("Number must be between 1 and 100")
        nr = checkinput(input("Choose number: "))

    r2 = random.randint(1, 100)
    print(r2)
    if nr == r2:
        #rc2 = random.choices("Amazing!", "Good job!", "Genie?", "Hacker?")
        #print(rc2)
        print("Amazing! +20")
    if nr != r2:
        print("Auwch, -10")
    hard()


diff = input("Choose level: ")


if diff == "easy":
    easy()

elif diff == "hard":
    hard()

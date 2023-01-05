import random

score = 100
r2 = 0
nr = 0

def checkinput(nmr, difficulty):
    global score
    if nmr == 'hard':
        hard()
    elif nmr == 'easy':
        easy()
    elif nmr == 'exit':
        exit()

    if nmr == 'hint':
        if difficulty == 'easy':
            print("It is easy enough...")
        elif difficulty == 'hard':
            if nmr < r2:
                print("It is bigger than ", (nr))
            elif nmr > r2:
                print("It's smaller than ", (nr))
        hard()

    while nmr == '' or nmr.isdigit() == False:
        print("Invalid, please make sure to enter a number.")
        nmr = input("Choose number: ")
        if nmr == 'hard':
            hard()
        elif nmr == 'easy':
            easy()
        elif nmr == 'exit':
            exit()

    ## From here we only check with integers
    nmr = int(nmr)
    if difficulty == "easy":
        if nmr >= 11 or nmr == 0:
            print("Number must be between 1 and 10!")
            checkinput(input("Choose number: "), "easy")
    elif difficulty == "hard":
        if nmr >= 101 or nmr == 0:
            print("Number must be between 1 and 100")
            checkinput(input("Choose number: "), "hard")

    return nmr


def easy():
    global score
    global nr
    nr = checkinput(input("Choose number: "), "easy")

    r1 = random.randint(1, 10);
    while True:

        if nr == r1:
            #random1 = random.choices("Amazing!", "Good job!", "Genie?", "Hacker?")
            #print(random1)
            print(r1)
            print("Good job! +20")
            score = score +20
            print(score)
            break
        elif nr != r1:
            print("Auwch, -10, try again")
            score = score -10
            print(score)
            if score <= 0:
                print("You lost, try again.")
                score = 100
                easy()
            nr = checkinput(input("Choose number: "), "easy")
    easy()


def hard():
    global score
    global r2
    global nr
    nr = checkinput(input("Choose number: "), "hard")

    r2 = random.randint(1, 100)
    while True:
        if nr == r2:
            #rc2 = random.choices("Amazing!", "Good job!", "Genie?", "Hacker?")
            #print(rc2)
            print("Amazing! +20")
            score = score +20
            print(score)
        elif nr != r2:
            print("Auwch, -10, try again")
            score = score -10
            print(score)
            if score <= 0:
                print("You lost, try again.")
                print("You'll start at easy:")
                score = 100
                easy()
            nr = checkinput(input("Choose number: "), "hard")
    hard()


diff = input("Choose level: ")


if diff == "easy":
    easy()

elif diff == "hard":
    hard()

import random


def easy():
    r1 = random.randint(1, 10);
    print(r1)

def difficult():
    r2 = random.randint(1, 100)
    print(r2)


diff = input("Choose level: ")

if diff == "easy":
    easy()

elif diff == "difficult":
    difficult()

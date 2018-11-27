import random

def dobbelsteen():
    min = 1
    max = 6
    return random.randint(min, max)

def yesno():
    while True:
        answer=input("yes or no? ")
        if answer =="yes":
            return True
        elif  answer =="no":
            return False
        else:
            print("retry")

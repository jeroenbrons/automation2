def doeIets(x):
    if x < 10:
        y ="x is kleiner dan 10"
    elif x >= 10 and x <20:
        y="x is tussen 10 en 20"
    else:
        y="x is groter dan 19"
    return y
invoer=int(input("geef getal"))
z=doeIets(invoer)

print(z)
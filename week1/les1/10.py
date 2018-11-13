num=int(input("geef getal"))
deel=int(input("geef deel"))
try:
    print(num/deel)
    
except ZeroDivisionError:
    print("door 0 delen mag niet")

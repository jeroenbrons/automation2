i=1
with open("11.txt","r") as tekst:
    for regel in tekst:
        print(str(i) + " " + regel)
        i=i+1
sample=[8,2,3,-1,7]
def highest(list):
    temp=0
    i=0
    while i < len(list):
        if list[i] > temp:
            temp=list[i]
        i=i+1
    return temp
print(highest(sample))

import matplotlib.pyplot as plt
x= [ 10,20,30]
y=['cats','dogs','fishes']
z=[.2,.1,0]
plt.pie(x, labels=y, explode=z)
plt.show()
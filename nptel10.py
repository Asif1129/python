import matplotlib.pyplot as plt
val=bins.values()
x=[]
y=[]
print(val)
for each in list(set(val)):
    x.append(each)
    y.append(val.count(each))
    print(each,val.count(each))
    plt.plot(x,y)
    plt.show()


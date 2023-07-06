import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[50,60,52,55,62]
plt.plot(x,y,color='red',linewidth=6,linestyle='dotted')
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Weather Chart")
plt.show()
plt.scatter(x,y)
plt.show()

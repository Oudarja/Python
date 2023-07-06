import matplotlib.pyplot as plt

days=[1,2,3,4,5,6]
max_t=[50,51,52,53,54,48]
min_t=[42,41,43,40,38,33]
avg_t=[(42+50)/2.0,(41+51)/2.0,(43+52)/2.0,(40+53)/2.0,(38+54)/2.0,(33+48)/2.0]
plt.plot(days,max_t,label="Max")
plt.plot(days,min_t,label="Min")
plt.plot(days,avg_t,label="Avg")
plt.legend(loc="best",shadow=True)
plt.grid()
plt.show()

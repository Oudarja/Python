import matplotlib.pyplot as plt

val=[300,500,1600,400,360]
label=['Price','Sell','Total','Shirt','Shari']
plt.pie(val,labels=label,radius=2,autopct='%.2f%%',shadow=True)
plt.show()

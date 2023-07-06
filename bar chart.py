import matplotlib.pyplot as plt
import numpy as np
product=np.array([1,2,3,4])
price=[15,25,40,30]
profit=[5,7,10,5]
plt.bar(product-.2,price,label='price',width=0.5,color='red')
plt.bar(product,profit,label='profit',width=0.5,color='blue')
plt.legend()
plt.show()

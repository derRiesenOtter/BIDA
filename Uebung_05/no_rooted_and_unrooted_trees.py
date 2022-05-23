import numpy as np 
import matplotlib.pyplot as plt

Taxa = np.arange(2,12+1)

plt.plot(Taxa,list(map(lambda x: x**2 ,Taxa)),'r',Taxa,list(map(lambda x: x**3 ,Taxa)),'b') 
plt.savefig("no_rooted_and_unrooted_trees",format ="pdf")
plt.show()
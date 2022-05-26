import matplotlib.pyplot as plt
import math

Taxa =range(3,12+1) 

plt.plot(Taxa,list(map(lambda x: math.factorial(((2*x)-5))/((2**(x-3))*math.factorial(x-3)) ,Taxa)),'r',Taxa,list(map(lambda x: math.factorial(((2*x)-3))/((2**(x-2))*math.factorial(x-2)) ,Taxa)),'b') 
plt.savefig("no_rooted_and_unrooted_trees",format ="pdf")
plt.show()
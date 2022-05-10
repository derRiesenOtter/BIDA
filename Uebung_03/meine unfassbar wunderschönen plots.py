
import numpy as np
import matplotlib.pyplot as plt

#Aufgabe 6
t = np.arange(-10,10+1) #  np.arange gibt gleichverteilte Werte aus

plt.plot(t,t**2) 
plt.savefig("BIDA_Python_Uebung_3_plot_x2")
plt.show() #danach wird ein neuer leerer Plot erstellt, deswegen muss savefig nach vorne

plt.plot(t,t**3) 
plt.savefig("BIDA_Python_Uebung_3_plot_x3")
plt.show()

plt.plot(t,t**2,'b',t,t**3,'r') 
plt.savefig("BIDA_Python_Uebung_3_plot_x2x3")
plt.show()

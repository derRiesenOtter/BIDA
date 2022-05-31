
from matplotlib import colors
import seaborn as sns
import matplotlib.pyplot as plt
import datatable as dt
#import pandas as pd

Algen = dt.fread("Algen.csv")
Algen_pandas = Algen.to_pandas()
sns.set_theme(style="whitegrid")

#Algen_pandas = pd.read_csv("Algen.csv") # bekomme so was anderes...

print (Algen_pandas)
sns.stripplot(x = Algen_pandas["Endocytobiose"],y=Algen_pandas["Anzahl (Hüll)-Membranen"], hue = Algen_pandas["Monophyletische Algen-Gruppe"], dodge =  True)
kokolores = ["blue","orange","green","red","purple","brown","pink","gray","yellow","cyan"]
for i in range(10):
    plt.text(s =Algen_pandas["Kürzel"][i], x = Algen_pandas["Endocytobiose"][i]+0.1*i-0.5, y= Algen_pandas["Anzahl (Hüll)-Membranen"][i]+0.02, color = kokolores[i])
plt.savefig("Algen Plot")
plt.show()


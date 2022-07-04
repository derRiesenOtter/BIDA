import seaborn as sns
import matplotlib.pyplot as plt
import datatable as dt

Tiere = dt.fread("Tiere.csv")
Tiere_pandas = Tiere.to_pandas()
sns.set_theme(style="whitegrid")

sns.stripplot(x = (Tiere_pandas["Gewicht"]),y=Tiere_pandas["Herzschlag"], hue = Tiere_pandas["Spezies"])
for i in range(15):
    plt.text(s = Tiere_pandas["Spezies"][i], x = (Tiere_pandas["Gewicht"][i]), y = (Tiere_pandas["Herzschlag"][i]))
plt.xlabel("Gewicht in g")
plt.ylabel("Herzfrequenz in min^-1")
plt.savefig("Tiere Plot")
plt.show()

#+0.1*i-0.5     [i]+0.02

import datatable as dt
import matplotlib.pyplot as plt
import seaborn as sns

df_Algen =  dt.fread("Algen.csv")
print(df_Algen)

print(df_Algen["Endocytobiose"])

sns.stripplot(x=df_Algen["Endocytobiose"],y = df_Algen["Anzahl (Hüll)-Membranen"])


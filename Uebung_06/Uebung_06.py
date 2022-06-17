import pandas as pd
import seaborn as sns

df_Algen = pd.read_csv("Algen.csv")
print(df_Algen)
sns.stripplot(x=1,y=2)
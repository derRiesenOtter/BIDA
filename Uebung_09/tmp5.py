import numpy as np
import pandas as pd

score_matrix = pd.DataFrame([[1,-1,-1,-1],[-1,1,-1,-1],[-1,-1,1,-1],[-1,-1,-1,1]])
score_matrix.columns = ["A","G","C","T"]
score_matrix.index = ["A","G","C","T"]
print(score_matrix["A"]["A"])
import pandas as pd
import numpy as np

df = pd.Series(['Jeep', 'Vitarela', 'Coca-Cola', 'Klabin', 'Samsung', np.nan, 'Unimed'], dtype=pd.StringDtype())

print(df.str.lower(), '\n')
print(df.str.upper(), '\n')
print(df.str.strip())

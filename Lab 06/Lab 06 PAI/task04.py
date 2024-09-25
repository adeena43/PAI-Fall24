import pandas as pd 
import numpy as np

data = {
    'title': ['Movie A', 'Movie B', 'Movie C', 'Movie D'],
    'revenue': [2.5, 0.5, 3.0, 1.2],
    'budget': [0.8, 0.3, 0.5, 1.0],
    'genre': ['Action', 'Drama', 'Comedy', 'Thriller'],
    'release_year': [2020, 2021, 2022, 2023]
}
df = pd.DataFrame(data)
df.index = np.arange(1, len(df)+1)
print(df)

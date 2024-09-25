import pandas as pd

data = {
    'title': ['Movie A', 'Movie B', 'Movie C', 'Movie D'],
    'revenue': [2.5, 0.5, 3.0, 1.2],
    'budget': [0.8, 0.3, 0.5, 1.0],
    'genre': ['Action', 'Drama', 'Comedy', 'Thriller'],
    'release_year': [2020, 2021, 2022, 2023]
}

df = pd.DataFrame(data)

print((df['revenue']>2) & (df['budget']<1))

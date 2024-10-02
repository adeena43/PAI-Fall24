import pandas as pd
df = pd.read_csv("heart (1).csv")
print(df[df["cp"]==2])

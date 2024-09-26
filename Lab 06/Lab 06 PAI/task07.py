import pandas as pd

df = pd.read_excel("employee.xlsx")
specific = df[df["Year_Joined"]==2018]
print(specific)
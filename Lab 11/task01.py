#from sklearn.datasets import heart_disease
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

df = pd.read_csv('heart.csv')
print(df.head())

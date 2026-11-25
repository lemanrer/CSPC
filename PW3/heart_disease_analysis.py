import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv("Heart_disease_cleveland_new.csv")

print(df.shape)
print(df.head())
print(df.describe())    
continuous = ["age", "chol", "trestbps", "thalach"]
data = df[continuous]

rng = np.random.default_rng(0)
data = rng.uniform(0, 10, 5000)
plt.hist(data, bins=25)
plt.xlabel("value")
plt.ylabel("how often")
plt.show()
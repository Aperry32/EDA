import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


#homes dataset file, locally saved
home_df = pd.read_csv("C:\\Users\\Arrington Perry\\EDA Project\\Data\\Homes dataset.csv")

#checking info & shape to understand the data better
#home_df.info()
#home_df.shape
#home_df.count()

#attemping to drop duplicates 
home_df = home_df.drop_duplicates()
#home_df.count()

#removing empty or null valued rows
home_df = home_df.dropna()
#home_df.info()

#checking histogram & pairplot for outliers and overall health
sns.pairplot(home_df)
plt.show()

#dropping feature HOA
home_df = home_df.drop(['HOA'], axis=1)
home_df.info()

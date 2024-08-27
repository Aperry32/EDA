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

#checking pairplot for outliers and overall health pre removal of dup & null values
sns.pairplot(home_df)
plt.show()

#attemping to drop duplicates 
home_df = home_df.drop_duplicates()
home_df.count()

#removing empty or null valued rows
home_df = home_df.dropna()
home_df.info()

#confirming all null values were removed from df
home_df.isnull()

#converting object features to floats or integers and then drop the replaced features from df
home_df['floor_covering_int'] = home_df['floor_covering'].astype('category').cat.codes
home_df['kitchen_features_int'] = home_df['kitchen_features'].astype('category').cat.codes
#home_df.info()

home_df = home_df.drop(['kitchen_features', 'floor_covering'], axis=1)
#home_df.info()

#bar graph of values after null value removal
home_df.sold_price.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))

#checking the correlation with a heatmap
corr = home_df.corr()
plt.figure(figsize=(10, 8))  # Adjust width and height for readability 
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
plt.show()

#checking pairplot for outliers and overall health
sns.pairplot(home_df)
plt.show()




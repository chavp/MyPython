import pandas as pd
import numpy as np

path = "ml-100k\\u.data"
df = pd.read_csv(path, sep='\t', names=['UserID', 'ItemID', 'Rating', 'Timestamp'])
print(type(df))
print(df.head())
print(df.columns)
print(df.shape)

import matplotlib.pyplot as plt
#lt.hist(df['Rating'])
#plt.show()
#print(df.groupby(['Rating'])['UserID'].count())

#plt.hist(df.groupby(['ItemID'])['ItemID'].count())
#plt.show()
#print(df.groupby(['ItemID'])['ItemID'].count())

n_users = df.UserID.unique().shape[0]
print('n_users:', n_users)

n_items = df['ItemID'].unique().shape[0]
print('n_items:', n_items)

ratings = np.zeros((n_users, n_items))
for row in df.itertuples():
	ratings[row[1]-1, row[2]-1] = row[3]
print('ratings:', ratings.shape)

sparsity = float(len(ratings.nonzero()[0]))
sparsity /= (ratings.shape[0] * ratings.shape[1])
sparsity *= 100
print('Sparsity: {:4.2f}%'.format(sparsity))

from sklearn.cross_validation import train_test_split
ratings_train, ratings_test = train_test_split(ratings,test_size=0.33,
random_state=42)

print('ratings_train:', ratings_train)
print('ratings_test:', ratings_test)

from sklearn.neighbors import NearestNeighbors
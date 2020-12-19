import pandas as pd
import numpy as np
import statsmodels.api as sm

df = pd.read_csv('veri.csv', encoding='utf-8')
df = df.drop(df.iloc[:,0:2], axis=1)
df = df.drop(df.iloc[:,-1:], axis=1)
maas = df.iloc[:,-1:]

df_linear = df.drop(df.iloc[:,0:2], axis=1)
X = df_linear.values
y = np.array(maas.values).reshape(-1,1)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X,y)

model = sm.OLS(lr.predict(X), X).fit()
print(model.summary())

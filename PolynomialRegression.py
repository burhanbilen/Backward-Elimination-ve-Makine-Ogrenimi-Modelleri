import pandas as pd
import numpy as np
import statsmodels.api as sm

df = pd.read_csv('veri.csv', encoding='utf-8')
df = df.drop(df.iloc[:,0:2], axis=1)
df = df.drop(df.iloc[:,-1:], axis=1)
maas = df.iloc[:,-1:]

df_polynomial = df.drop(df.iloc[:,1:2], axis=1)
X = df_polynomial.values
y = np.array(maas.values).reshape(-1,1)

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
pr = PolynomialFeatures(degree = 2)
x_poly = pr.fit_transform(X)
lr2 = LinearRegression()
lr2.fit(x_poly,y)

model = sm.OLS(lr2.predict(pr.fit_transform(X)), X).fit()
print(model.summary())

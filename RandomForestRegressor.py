import pandas as pd
import numpy as np
import statsmodels.api as sm

df = pd.read_csv('veri.csv', encoding='utf-8')
df = df.drop(df.iloc[:,0:2], axis=1)
df = df.drop(df.iloc[:,-1:], axis=1)
maas = df.iloc[:,-1:]

df_randomforest = df.drop(df.iloc[:,0:2], axis=1)
X = df_randomforest.values
y = np.array(maas.values).reshape(-1,1)

from sklearn.ensemble import RandomForestRegressor
rf=RandomForestRegressor(n_estimators = 10,random_state=0)
rf.fit(X,y.ravel())

model = sm.OLS(rf.predict(X), X).fit()
print(model.summary())

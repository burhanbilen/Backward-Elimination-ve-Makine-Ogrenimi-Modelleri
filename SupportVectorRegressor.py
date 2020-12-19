import pandas as pd
import numpy as np
import statsmodels.api as sm

df = pd.read_csv('veri.csv', encoding='utf-8')
df = df.drop(df.iloc[:,0:2], axis=1)
df = df.drop(df.iloc[:,-1:], axis=1)
maas = df.iloc[:,-1:]

df_svr = df.drop(df.iloc[:,0:2], axis=1)
X = df_svr.values
y = np.array(maas.values).reshape(-1,1)

from sklearn.preprocessing import StandardScaler
sc1=StandardScaler()
X_olcekli = sc1.fit_transform(X)
sc2=StandardScaler()
y_olcekli = sc2.fit_transform(y)

from sklearn.svm import SVR
svr = SVR(kernel='rbf')
svr.fit(X_olcekli, y_olcekli)

model = sm.OLS(svr.predict(X_olcekli), X_olcekli).fit()
print(model.summary())

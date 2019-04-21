from math import sqrt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error
from pyramid.arima import auto_arima
from statsmodels.tsa.stattools import adfuller

df = pd.read_csv('RAIN_BANGALORE.csv', delimiter='\t')
months = list(df.columns.values)[1:]
dates = []
rain = {'RAIN': []}
avg = {}
for m in months:
  avg[m] = df[m].mean()
for i, row in df.iterrows():
	dates.append(pd.Timestamp(row['Year'].astype(int), 6, 1))
	if row['Jun'] != 0:
	  rain['RAIN'].append(row['Jun'])
	else:
	  rain['RAIN'].append(avg['Jun'])  


data = pd.DataFrame(data=rain, index=dates)
print data.head()
plt.plot(data)
train = data.loc['1901-06-01':'1980-06-01']
test = data.loc['1981-06-01':]
history = train
predictions = {'RAIN': []}
for i, row in test.iterrows():
   model = ARIMA(history, order=(8,0,6))
   model_fit = model.fit(disp=0)
   fore = model_fit.forecast()[0]
   predictions['RAIN'].append(fore)
   history.loc[i] = row['RAIN']

predictions = pd.DataFrame(data=predictions['RAIN'], index=test.index)
print predictions[:'2001-01-01']
error = mean_squared_error(test, predictions)
print('ARMA Test RMSE: %.2f' % sqrt(error))

# plot
plt.plot(test)
plt.plot(predictions, color='yellow')
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("TEMP_ALLAHABAD.csv", delim_whitespace=True)
dates = []
time_temp = {'TEMP': []}
months = list(df.columns.values)[1:]
for i, row in df.iterrows():
	for m in range(1, 13):
		dates.append(pd.Timestamp(row['Year'].astype(int), m, 1))
	for m in months:
		time_temp['TEMP'].append(row[m])
data = pd.DataFrame(data=time_temp, index=dates)

train = data.loc['1901-01-01':'1980-12-01']
test = data.loc['1981-01-01':]
history = train
predictions = {'TEMP': []}
for i, row in test.iterrows():
   model = ARIMA(history, order=(1,0,1))
   model_fit = model.fit(disp=0)
   fore = model_fit.forecast()[0]
   predictions['TEMP'].append(fore)
   history.loc[i] = row['TEMP']

predictions = pd.DataFrame(data=predictions, index=test.index)   
error = mean_absolute_error(test, predictions['TEMP'])
print 'ARMA'
print('Test MAE: %.2f' % error)

plt.plot(test)
plt.plot(predictions, color='red')
plt.show()

# coding: utf-8

# In[1]:


# USING NAIVE BAYES FUZZY LOGIC
def rainfall(rain):
    if rain>=62 and rain<=87:
        return 'very good'
    elif (rain>=50 and rain<62) or (rain>87 and rain<=100):
        return 'good'
    elif (rain>=25 and rain<50) or (rain>100 and rain<=150):
        return 'average'
    elif (rain>=10 and rain<25) or (rain>150 and rain<=200):
        return 'bad'
    else:
        return 'very bad'
def temperature(temp):
    if temp>=20 and temp<=25:
        return 'very good'
    elif (temp>=15 and temp<20):
        return 'good'
    elif (temp>=12 and temp<15) or (temp>25 and temp<=33):
        return 'average'
    elif (temp>=8 and temp<12) or (temp>33 and temp<=40):
        return 'bad'
    else:
        return 'very bad'
def pred(rain,temp):
    if (rain=='very good' and temp=='very good') or (rain=='very good' and temp=='good'):
        return 'very good'
    if (rain=='very good' and temp=='bad') or (rain=='very good' and temp=='average'):
        return 'good'
    if (rain=='very good' and temp=='bad') or (rain=='very good' and temp=='very bad'):
        return 'average'
    if (rain=='good' and temp=='very good') or (rain=='good' and temp=='good'):
        return 'good'
    if (rain=='good' and temp=='bad') or (rain=='good' and temp=='average'):
        return 'good'
    if (rain=='good' and temp=='bad') or (rain=='good' and temp=='very bad'):
        return 'average'
    if (rain=='average' and temp=='very good') or (rain=='average' and temp=='good'):
        return 'average'
    if (rain=='average' and temp=='bad') or (rain=='average' and temp=='average'):
        return 'average'
    if (rain=='average' and temp=='bad') or (rain=='average' and temp=='very bad'):
        return 'bad'
    if (rain=='bad' and temp=='very good') or (rain=='bad' and temp=='good'):
        return 'bad'
    if (rain=='bad' and temp=='bad') or (rain=='bad' and temp=='average'):
        return 'bad'
    if (rain=='bad' and temp=='bad') or (rain=='bad' and temp=='very bad'):
        return 'very bad'
    if (rain=='very bad' and temp=='very good') or (rain=='very bad' and temp=='good'):
        return 'very bad'
    if (rain=='very bad' and temp=='bad') or (rain=='very bad' and temp=='average'):
        return 'very bad'
    if (rain=='very bad' and temp=='bad') or (rain=='very bad' and temp=='very bad'):
        return 'very bad'

arain = []
atemp = []
import pandas as pd
data = pd.read_csv('temp_alld.csv', delim_whitespace=True, index_col=0)

for x in range(1997, 2002):
	avgt = data.loc[str(x)+'-11-01':str(x+1)+'-03-01'].sum()
	avgt /= 5
	atemp.append(float(avgt))

data = pd.read_csv('rain_alld.csv', delim_whitespace=True, index_col=0)

for x in range(1997, 2002):
	avgr = data.loc[str(x)+'-01-01':str(x)+'-12-01'].sum()
	avgr /= 12
	arain.append(float(avgr))	
print arain
print atemp    
year=1997
print("YEAR YIELD")
for i in range(5):
    frain=rainfall(arain[i]) 
    ftemp=temperature(atemp[i])
    prediction=pred(frain,ftemp)
    print(year,prediction)
    year=year+1


# from matplotlib import pyplot
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt
import pandas as pd


dataset= pd.read_csv("fypdataset.csv")

def crime_prediction(city, crime, year):
    global dataset
    df = dataset[dataset['department_name'] == city]
    history_crime = [int(x) for x in df[crime]]
    # history_years = list(range(1975,2016))

    year_pred = year - 2015
    predictionsList = []


    for t in range(year_pred):
        model = ARIMA(history_crime, order=(1,1,0))
        model_fit = model.fit()
        output = model_fit.forecast()
        yhat = output[0]
        # predictionsList.append(yhat)
        # obs = int(test_history[t])
        history_crime.append(yhat)
    
    
    return yhat
    



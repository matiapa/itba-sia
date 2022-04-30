import numpy as np 


# Function for standardization 
def standarizedf(dataframe): 
    x = dataframe.transpose()
    mu = []
    sigma = [] 
    for t in range(len(x)):  
        mu.append(np.mean(x[t]))
        sigma.append(np.std(x[t]))
        x[t] = (x[t] - np.mean(x[t]))/np.std(x[t])
    return x.transpose(), mu, sigma

def destandarizedf(dataframe, mu, sigma):
    x = dataframe.transpose()
    for t in range(len(x)):
        x[t] = x[t]*sigma[t] + mu[t]
    return x.transpose()

# Functions for scaling and descaling using range  
def scaledf(dataframe): 
    x = dataframe.transpose()
    min = []
    max = [] 
    for t in range(len(x)):
        min.append(np.min(x[t]))
        max.append(np.max(x[t]))  
        x[t] = (x[t] - np.min(x[t]))/(np.max(x[t]) - np.min(x[t]))
    return x.transpose(), min, max

def descaledf(dataframe, min, max):
    x = dataframe.transpose()
    for t in range(len(x)):  
        x[t] = x[t]*(max[t]-min[t])+min[t]
    return x.transpose()
import sys
sys.path.append("..")

from oja.network import Oja
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas
from matplotlib import pyplot as plt

# Parameters definition

numeric_columns = ["Area","GDP","Inflation","Life.expect","Military","Pop.growth","Unemployment"]
eta = 0.005
iterations = 100
real_first_comp = [0.08, -0.33, 0.27, -0.32, 0.13, -0.32, 0.18]

# Read the data

df = pandas.read_csv('../in/europe.csv')
labels = df["Country"].to_numpy()

df.drop("Country", axis=1, inplace=True)
inputs = StandardScaler().fit_transform(df.values)

# Train the network

oja = Oja(eta, iterations)

w0 = np.random.random(size=len(inputs[0])) * 2 - 1

weights = oja.train(w0, inputs)

# Show the results

print(f"First component coordinates: {weights[-1]}")

errors = [np.linalg.norm(wt - real_first_comp) for wt in weights]

plt.plot(range(iterations), errors)
plt.ylabel('Error')
plt.xlabel('Iteration')
plt.show()
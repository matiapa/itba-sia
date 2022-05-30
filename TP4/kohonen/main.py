import sys
sys.path.append("..")

from kohonen.neuron import Neuron
from kohonen.network import Kohonen
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas
from matplotlib import cm
import matplotlib.pyplot as plt
from adjustText import adjust_text

# Parameters definition

k = 5
r0 = 10
n0 = 1
numeric_columns = ["Area","GDP","Inflation","Life.expect","Military","Pop.growth","Unemployment"]

# Read the data

df = pandas.read_csv('../in/europe.csv')
labels = df["Country"].to_numpy()

df.drop("Country", axis=1, inplace=True)
inputs = StandardScaler().fit_transform(df.values)

# Train the network

kohonen = Kohonen(k, r0, n0)

kohonen.train(inputs)

# Show the results

def label_plot():
    xs, ys = [], []
    texts = []
    for i in range(len(inputs)):
        x, y = kohonen.get_coords(inputs[i])
        xs.append(x)
        ys.append(y)
        texts.append(plt.text(x, y, labels[i]))
    plt.scatter(xs, ys)
    adjust_text(texts, only_move={'points':'y', 'texts':'y'}, arrowprops=dict(arrowstyle="->", color='r', lw=0.5))
    plt.show()

def count_plot():
    heatmap = np.zeros((k, k))
    for input in inputs:
        x, y = kohonen.get_coords(input)
        heatmap[y][x] += 1
    plt.imshow(heatmap)
    plt.colorbar()
    plt.show()

def var_avg_plot():
    count_matrix = np.ones((k, k))
    vars_avg_matrix = np.zeros((len(numeric_columns), k, k))

    # Sum the values of variables
    for input in inputs:
        x, y = kohonen.get_coords(input)
        count_matrix[y][x] += 1
        for v in range(len(numeric_columns)):
            vars_avg_matrix[v][y][x] += kohonen.network[y][x].weights[v]

    # Divide by the cell count
    for v in range(len(numeric_columns)):
        vars_avg_matrix[v] /= count_matrix

    # Display all matrixes as heatmaps
    _, axes = plt.subplots(2,4)
    for v in range(len(numeric_columns)):
        axes[v//4][v%4].set_title(numeric_columns[v])
        axes[v//4][v%4].imshow(vars_avg_matrix[v], cmap=cm.gray)
    plt.show()

def u_matrix_plot():
    heatmap = np.zeros((k, k))
    for x in range(k):
        for y in range(k):
            own_weights = kohonen.network[y][x].weights
            avg_neigh_dist = 0
            # print("--------------------------")
            # print(f"O({x},{y})")

            valid_neighs = 0
            for nx in range(x-1, x+2):
                for ny in range(y-1, y+2):
                    if nx>0 and nx<k and ny>0 and ny<k:
                        # print(f"N({nx},{ny}): {kohonen.network[ny][nx].distance(own_weights)}")
                        avg_neigh_dist += kohonen.network[ny][nx].distance(own_weights)
                        valid_neighs += 1
        
            heatmap[y][x] = avg_neigh_dist / valid_neighs
    print(f"Avg {sum(heatmap[y][x] for y in range(k) for x in range(k))/k**2}")

    plt.imshow(heatmap, cmap=cm.gray)
    plt.colorbar()
    plt.show()

label_plot()
count_plot()
u_matrix_plot()
var_avg_plot()
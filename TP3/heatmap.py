#!/usr/bin/python3
# 3D Heatmap in Python using matplotlib
  
# to make plot interactive
  
# importing required libraries
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pylab import *
  
# reading a dummy dataset
dataset = pd.read_csv("TP3/inputs/TP3-ej2-Conjunto-entrenamiento.txt", sep="   ")
dataset_output = pd.read_csv("TP3/inputs/TP3-ej2-Salida-deseada.txt", sep="   ")

x = dataset["x"].tolist()
y = dataset["y"].tolist()
z = dataset["z"].tolist()
  
colo = dataset_output["output"].tolist()
  
# creating 3d figures
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111, projection='3d')
  
# configuring colorbar
color_map = cm.ScalarMappable(cmap=cm.viridis)
color_map.set_array(colo)
  
# creating the heatmap
img = ax.scatter(x, y, z, marker='s', 
                 s=99, color='gray')
plt.colorbar(color_map)
  
# adding title and labels
ax.set_title("3D Heatmap")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('')
  
# displaying plot
plt.show()
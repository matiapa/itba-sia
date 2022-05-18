import sys


import sys
sys.path.append("..")

import pandas
from kohonen.network import Kohonen

if __name__ == '__main__':
    k = 10
    r0 = 10
    n0 = 1

    kohonen = Kohonen(k, r0, n0)

    df = pandas.read_csv('../in/europe.csv')
    labels = df["Country"].to_numpy()
    inputs = df[["Area","GDP","Inflation","Life.expect","Military","Pop.growth","Unemployment"]].to_numpy()

    kohonen.train(inputs)
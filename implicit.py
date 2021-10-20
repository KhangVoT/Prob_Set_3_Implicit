# Module Name: explicit
# Author: Khang Vo
# Date Created: 10/17/2021
# Date Last Modified: 10/17/2021
# Python Version: 3.9

import os

import pandas as pd
import numpy as np


def calc(nx, nt):

    if type(nx) == int or type(nx) == float:
        nx = [nx]
    if type(nt) == int or type(nt) == float:
        nt = [nt]

    for index in range(len(nx)):
        a = pd.read_csv("A_" + str(nx[index]) + "_" + str(nt[index]) + ".txt",
                        sep="\t", index_col=0, header=0)
        a.columns = a.columns.astype(float)

        b = pd.read_csv("b_" + str(nx[index]) + "_" + str(nt[index]) + ".txt",
                        sep="\t", index_col=0, header=0)
        b.columns = b.columns.astype(float)

        for n in range(len(b.index) - 1):
            b.iloc[n + 1, :] = np.linalg.solve(a, b.iloc[n, :])
        x = b

        x.to_csv("x_" + str(nx[index]) + "_" + str(nt[index]) + ".txt", sep="\t")


if __name__ == "__main__":
    root = os.getcwd() + "/files"
    os.chdir(root)

    # setup number of nodes for both x and t
    nx = 100, 200, 300
    nt = 400, 500, 600
    calc(nx, nt)

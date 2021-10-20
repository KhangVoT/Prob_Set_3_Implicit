# Module Name: plot_timestep
# Author: Khang Vo
# Date Created: 10/17/2021
# Date Last Modified: 10/19/2021
# Python Version: 3.9

import os
import math
import warnings

import pandas as pd
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')


def plot_static_axis(nx, nt):

    if type(nx) == int or type(nx) == float:
        nx = [nx]
    if type(nt) == int or type(nt) == float:
        nt = [nt]

    t = dict()

    for index in range(len(nx)):
        t[index] = pd.read_csv("x_" + str(nx[index]) + "_" + str(nt[index]) + ".txt",
                               sep="\t", index_col=0, header=0)
        t[index].columns = t[index].columns.astype(float)

    t_keys = t.keys()
    for i in range(len(t_keys)):
        # subplot 1 with nx/nt parameters
        plt.figure(1)
        plt.subplot(1, len(t_keys), i + 1)
        for count in range(0, len(t[i].index)):
            if count | 0 and count % 3 == 0:
                plt.plot(t[i].columns.tolist(), t[i].iloc[count, :], color="black", linewidth=0.25)
                plt.xlabel("x [m]")
                plt.ylabel("T [deg. C]")
                plt.ylim(300, 1200)
                plt.title("Temperature evolution " + str(nx[i]) + "_" + str(nt[i]))
                plt.draw()
                plt.pause(0.1)
    plt.show()


def plot_dynamic_axis(nx, nt):

    if type(nx) == int or type(nx) == float:
        nx = [nx]
    if type(nt) == int or type(nt) == float:
        nt = [nt]

    # Physical parameters
    kappa = 1e-6  # rock thermal diffusivity [m2/s]

    t = dict()

    for index in range(len(nx)):
        t[index] = pd.read_csv("x_" + str(nx[index]) + "_" + str(nt[index]) + ".txt",
                               sep="\t", index_col=0, header=0)
        t[index].columns = t[index].columns.astype(float)

    t_keys = t.keys()
    for i in range(len(t_keys)):
        # subplot 1 with nx/nt parameters
        plt.figure(1)
        plt.subplot(1, len(t_keys), i + 1)
        for count in range(0, len(t[i].index)):
            if count | 0 and count % 3 == 0:
                norm = t[i].columns / math.sqrt(kappa * t[i].index[count])
                plt.plot(norm, t[i].iloc[count, :], color="black", linewidth=0.25)
                plt.xlabel("x [m]")
                plt.xlim(min(norm), max(norm))
                plt.ylabel("T [deg. C]")
                plt.ylim(min(t[i].iloc[count, :]), max(t[i].iloc[count, :]))
                plt.title("Temperature evolution " + str(nx[i]) + "_" + str(nt[i]))
                plt.draw()
                plt.pause(0.1)
    plt.show()


if __name__ == "__main__":
    root = os.getcwd() + "/files"
    os.chdir(root)

    # setup number of nodes for both x and t
    nx = 100, 200, 300
    nt = 400, 500, 600
    plot_static_axis(nx, nt)
    plot_dynamic_axis(nx, nt)

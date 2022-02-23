from operator import index
from turtle import right
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Y_VALUES = [5, 10, 20, 50, 100, 150, 250, 500, 1000, 1500, 2000, 2500, 2750, 3250]

data = pd.read_csv("frequency_data.csv")


def plot_hist (title, sum, x, y=-1, yInterval=250, xLabel="Correct Answers Weighted"):
    values = plt.hist (sum, bins=[bin for bin in range(x)], edgecolor="black", zorder=3)
    if y == -1:
        max = np.max(values[0])
        for num in Y_VALUES:
            if max < num:
                yInterval = num/5
                y = num + yInterval
                break

    plt.title (title)
    plt.xlabel (xLabel)
    plt.ylabel ("Number of Entries")
    plt.xticks (np.arange(0, x, 1))
    plt.yticks (np.arange(0, y, yInterval))
    plt.grid (axis="y", alpha=0.75, zorder=0)
    plt.show ()


def plot_know_2 ():
    plot_hist ("2 Group Knowledge Weighted Sum", data["2_group_know_weighted_sum"], 13, 2500)

def plot_know_3 ():
    plot_hist ("3 Group Knowledge Weighted Sum", data["3_group_know_weighted_sum"], 13, 2500)


def plot_knowinf_2 ():
    plot_hist ("2 Group Knowledge Info Weighted Sum", data["2_group_knowinf_weighted_sum"], 11, 2750)

def plot_knowinf_3 ():
    plot_hist ("3 Group Knowledge Info Weighted Sum", data["3_group_knowinf_weighted_sum"], 11, 2750)


def plot_behav_2 ():
    plot_hist ("2 Group Behavior Weighted Sum", data["2_group_behav_weighted_sum"], 10, 2500)

def plot_behav_3 ():
    plot_hist ("3 Group Behavior Weighted Sum", data["3_group_behav_weighted_sum"], 9, 2750)


def plot_behav7_2 ():
    plot_hist ("2 Group Behavior 7 Days Weighted Sum", data["2_group_behav7_weighted_sum"], 5, 3250)

def plot_behav7_3 ():
    plot_hist ("3 Group Behavior 7 Days Weighted Sum", data["3_group_behav7_weighted_sum"], 5, 3250)

def create_plots ():
    plot_know_2 ()
    plot_know_3 ()
    plot_knowinf_2 ()
    plot_knowinf_3 ()
    plot_behav_2 ()
    plot_behav_3 ()
    plot_behav7_2 ()
    plot_behav7_3 ()



def behav_sum_groups ():
    for i in range(8):
        behav_sum = data[(data["3_group_behav_weighted_sum"] >= i) & (data["3_group_behav_weighted_sum"] < i+1)]
        plot_hist (f"Knowledge Sum for Behavior {i}", behav_sum["3_group_know_weighted_sum"], 13, -1, xLabel="Knowledge Sum Weighted")


def stacked_behavior_know_sum ():
    arr = [[0 for x in range(8)] for x in range(12)]

    for i in range(8):
        behav_i_know = data[(data["3_group_behav_weighted_sum"] >= i) & (data["3_group_behav_weighted_sum"] < i+1)]
        for j in range(12):
            know_sums = behav_i_know[(behav_i_know["3_group_know_weighted_sum"] >= j) & (behav_i_know["3_group_know_weighted_sum"] < j+1)]
            if (not know_sums.empty):
                arr[j][i] = know_sums.shape[0]

    stackedData = pd.DataFrame(arr)
    print (stackedData)
    # columns=[f"Behavior {i}" for i in range(8)], index=[f"Knowledge {i}" for i in range(12)]

    stackedData.plot (kind="bar", stacked=True, zorder=3)
    plt.title ("How People's Knowledge Relates To Their Behavior")
    plt.legend (title="Weighted Behavior Sum")
    plt.xticks (rotation=0)
    plt.yticks (np.arange(0, 2500, 250))
    plt.xlabel ("Weighted Knowledge Sum")
    plt.ylabel ("Number of Entries")
    plt.grid (axis="y", alpha=0.75, zorder=0)

    plt.show ()

stacked_behavior_know_sum ()
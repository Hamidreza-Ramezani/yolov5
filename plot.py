from __future__ import annotations
import json
from statistics import median
import matplotlib.pyplot as plt
from os import walk
import numpy as np
import itertools

#FREQS = ["medium", "high"]
FREQS = ["high"]
DATA_DIR = "./"
#MODELS = ["squeezenet", "mobilenetv2", "alexnet", "googlenet", "inception3", "resnet", "shufflenetv2"]
MODELS = ["YOLOv5"]
DATA = ["runtime"]

def ave(x):
    x.sort() 
    half_list = int(len(x)//2)
    upper_quartile = median(x[-half_list:])
    lower_quartile = median(x[:half_list])
    half_quartile = median(x)
    print(lower_quartile, half_quartile, upper_quartile)
    return (upper_quartile + lower_quartile + half_quartile)/3

for model in MODELS:
    fig, axs = plt.subplots(1,1)
    fig.suptitle(f'Vision Model: {model}')
    filenames = 'runtime.txt'
    my_file = open("runtime.txt", "r+")
    collected_data = []
    for line in my_file:
        collected_data.append(float(line))
    axs.boxplot(collected_data, showfliers=False)
    axs.set_ylabel('Runtime ms')
    axs.set_xlabel(f'Frequency: {FREQS}')
    axs.spines['right'].set_visible(False)
    axs.spines['top'].set_visible(False)
    annotStr = ""
    annotStr += " med: {:.2f} Change Percentage: {:.2f}%\n".\
        format(median(collected_data), (max(collected_data) - min(collected_data)) * 100 / max(collected_data))
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    axs.text(0.01, 0.99, annotStr, transform=axs.transAxes, fontsize=10, bbox=props)
    plt.show()

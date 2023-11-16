import matplotlib.pyplot as plt
import numpy as np
from read_data import ReadData


class Task:
    def __init__(self):
        print("hi")

    def show(self):
        d = ReadData()
        data = d.query()
        xpoints = np.array([0, 6])
        ypoints = np.array([0, 250])

        plt.plot(xpoints, data)
        plt.show()
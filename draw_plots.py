import os
import pandas as pd
import matplotlib.pyplot as plt

class PlotDrawing:
    def __init__(self):
        self.plot_directory = "plots"

    def draw_plots(self, data):
        os.makedirs(self.plot_directory, exist_ok=True)
        plot_paths = []

        for column in data.columns:
            plt.figure(figsize=(10, 6))
            plt.plot(data[column])
            plt.title(column)
            plt.xlabel("index")
            plt.ylabel("value")

            plot_path = os.path.join(self.plot_directory, f"{column}.png")
            plt.savefig(plot_path)
            plot_paths.append(plot_path)

        return plot_paths

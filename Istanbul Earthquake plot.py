#This ode uses data gathered by znl_arad from earthquake data bases for Istanbul region from 1800 until today
#This code is written by znl_arad

import pandas as pd
import matplotlib.pyplot as plt
import json


data = pd.read_csv("dataset.csv")


x=data["time"]
y=data["mag"]


plt.figure(figsize=(20, 6))  # Adjust the figure size as needed
plt.plot(x, y, marker='o', linestyle='-')
plt.xlabel("Date")
plt.ylabel("Magnitude")
plt.title("CSV Data Plot")
plt.grid(True)
plt.show()
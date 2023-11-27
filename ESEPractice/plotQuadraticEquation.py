#Q2 B (I dont remember full)
#we have to plot the line or curve for the quadratic equation in range [-5: 5] and plot a bar chart for some company
import matplotlib.pyplot as plt
import numpy as np

x = np.array([i for i in range(-5, 6)])
y = np.array([i**2 for i in range(-5, 6)])

plt.bar(x, y)
plt.show()
import matplotlib.pyplot as plt

x_values = [0, 1, 2, 3, 4, 5]
square = [0, 1, 4, 9, 16, 25]
plt.plot(x_values, square)

plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()
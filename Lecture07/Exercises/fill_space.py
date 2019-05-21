import matplotlib.pyplot as plt

x_values = list(range(11))
squares = [x**2 for x in x_values]
cubes = [x**3 for x in x_values]

plt.scatter(x_values, squares, c='blue', edgecolor='none', s=20)
plt.scatter(x_values, cubes, c='red', edgecolor='none', s=20)

plt.fill_between(x_values, cubes, squares, facecolor='blue', alpha=0.25)

plt.axis([0,11,0,1100])
plt.show()
import matplotlib.pyplot as plt

x_values = list(range(1000))
squares = [x**2 for x in x_values]
plt.scatter(x_values, squares, c=squares, cmap=plt.cm.Blues, edgecolor='none', s=10)

plt.scatter(x_values[0], squares[0], c='green', edgecolor='none', s=100)
plt.scatter(x_values[-1], squares[-1], c='red', edgecolor='none', s=100)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=18)
plt.ylabel("Square of Value", fontsize=18)
plt.tick_params(axis="both", which="major", labelsize=14)

plt.show()
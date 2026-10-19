
import numpy as np
import matplotlib.pyplot as plt

# Given data points
x = np.array([1, 2, 3])
y = np.array([2, 10, 26])

# Lagrange interpolation function
def lagrange(x_data, y_data, x_value):
    n = len(x_data)
    result = 0.0

    for i in range(n):
        term = y_data[i]

        for j in range(n):
            if i != j:
                term *= (x_value - x_data[j]) / (x_data[i] - x_data[j])

        result += term

    return result

# Predict value
x_value = 2.5
y_value = lagrange(x, y, x_value)

print(f"Interpolated value at x = {x_value}: {y_value:.4f}")

# Plot
x_plot = np.linspace(min(x), max(x), 200)
y_plot = [lagrange(x, y, xi) for xi in x_plot]

plt.scatter(x, y, color="red", label="Data Points")
plt.plot(x_plot, y_plot, color="blue", label="Lagrange Polynomial")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Lagrange Interpolation")
plt.legend()
plt.grid(True)
plt.show()

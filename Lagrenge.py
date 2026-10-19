
import numpy as np
import matplotlib.pyplot as plt

# Given data points
x_points = np.array([1, 2, 3])
y_points = np.array([2, 10, 26])

# Lagrange interpolation function
def lagrange_interpolation(x, x_points, y_points):
    n = len(x_points)
    result = 0

    for i in range(n):
        term = y_points[i]

        for j in range(n):
            if j != i:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])

        result += term

    return result

# Generate x value for smoot curve
x_value = np.linspace(1, 5, 200)
#calculate interpolated y value
y_value = []

# Plot
for x in x_value:
    y = lagrange_interpolation(x, x_points, y_points)
    y_value.append(y)

plt.scatter(x_points, y_points, color="red", label="Data Points")

plt.plot(x_value, y_value, color="green", label="Lagrange Polynomial")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Lagrange Interpolation")
plt.legend()
plt.grid(True)

#plt _Value
plt.show()

import pandas as pd
df = pd.DataFrame({
    'x_values': x_value, 
    'y_values': y_value,   
    
})
print(df)
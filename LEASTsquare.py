import numpy as np
import matplotlib.pyplot as plt

#simple data
x = np.array([1,2,3,4,5])
y = np.array([2,4,5,4,5])
n=len(x)

#Apply formula
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x*y)
sum_x2 = np.sum(x*x)

a = (n * sum_xy - sum_x *sum_y)/(n * sum_x2 - sum_x **2) # slope
b = (sum_y - a * sum_x)/n                               # Intercept

print(f"Slope (a): {a:.2f}")
print(f"Intercept (b): {b:.2f}")

#Predicted Values
y_pred = a * x + b

#Plot
plt.scatter(x, y, color= "red",label = "Data Points")
plt.plot(x, y_pred, color= "blue",label = "Best-fit Line")
plt.legend()
plt.show()
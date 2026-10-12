import numpy as np
import matplotlib.pyplot as plt

#sample data
x = np.array([1,2,3,4,5], dtype=float)
y = np.array([2.2,2.8,7.6,12.5,20.1], dtype=float)

#Degree of polynomial
n = 2
m = len(x)
# step 1 : computer requird summations
Xsum = [np.sum(x**k) for k in range (2*n + 1)]
Ysum = [np.sum((x**k) * y) for k in range (n + 1)]

A = np.zeros((n+1,n+1))
B = np.zeros(n+1)

for i in range(n+1):
    for j in range(n+1):
        A[i,j] = Xsum[i + j]
    B[i] = Ysum[i]
    
#step 3 : solve for coefficents
a = np.linalg.solve(A, B)
print("polynomial coeffcients(a0, a1, a2).....",a)

#step 4 : Predict value
y_pred = np.zeros_like(x)
for i in range(n+1):
    y_pred += a[i] * (x ** i)

#step 5 : Plot
plt.scatter(x, y, label = "Data Points")
plt.plot(x, y_pred, color= "red",label = f"Degree {n} fit")
plt.legend()
plt.show()
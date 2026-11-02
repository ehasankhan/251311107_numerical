def func(x):
    return 1 / (1 + x * x)

def trapezoidal_rule(Xo,Xn,n):
    h = (Xn - Xo) / n
    total = func (Xo) + func (Xn)

    for i in range(1,int (n)):
        total = total + func(Xo + i * h)
        
    return(h / 2) * total

#-------- Input section --------
Xo = float(input("Enter lower limit (Xo): "))
Xn = float(input("Enter upper limit (Xn): "))
n = int(input("Enter number of intervals (n): "))

#------ Calculation ---------
print("=> By using Trapezoidal Rule: ")
ans = trapezoidal_rule(Xo, Xn, n)
print("Approximate integration :- {ans:.5f} ")